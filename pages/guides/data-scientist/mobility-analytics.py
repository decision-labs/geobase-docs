#! /usr/bin/env python

import movingpandas as mpd
import pandas as pd
import h3
import opendatasets as od
import os
import geopandas as gpd
from shapely.geometry import Point, Polygon
from datetime import datetime, timedelta
from p_tqdm import p_umap
from tqdm.notebook import tqdm
tqdm.pandas()

input_file_path = 'taxi-trajectory/train.csv'


def get_porto_taxi_from_kaggle():
    if not os.path.exists(input_file_path):
        od.download("https://www.kaggle.com/datasets/crailtap/taxi-trajectory")


get_porto_taxi_from_kaggle()
# Read the raw data
df = pd.read_csv(input_file_path, nrows=10, usecols=[
                 'TRIP_ID', 'TAXI_ID', 'TIMESTAMP', 'MISSING_DATA', 'POLYLINE'])

# Convert polyline string to list
df.POLYLINE = df.POLYLINE.apply(eval)

# Remove missing data records
df = df.query("MISSING_DATA == False")

# Calculate the length of the polyline
df["geo_len"] = df["POLYLINE"].apply(lambda x: len(x))

# Remove records with no polyline
df.drop(df[df["geo_len"] == 0].index, axis=0, inplace=True)

# print logs of this check point of creating a data frame with the raw data plus the polyline length
print(
    f"Created a data frame with the raw data plus the polyline length\n: {df.head()}")


def unixtime_to_datetime(unix_time):
    return datetime.fromtimestamp(unix_time)


# Compute the datetime from the timestamp and the running number
def compute_datetime(row):
    unix_time = row['TIMESTAMP']
    offset = row['running_number'] * timedelta(seconds=15)
    return unixtime_to_datetime(unix_time) + offset


"""
The explode() function in pandas is used to transform lists within a DataFrame cell into separate rows. Let me explain with an example:
Let's say your original DataFrame df looks like this:

```
POLYLINE
   TRIP_ID  TAXI_ID            POLYLINE
0        1      123  [[1,2], [3,4], [5,6]]
1        2      456  [[7,8], [9,10]]
```

If you apply the explode() function to the POLYLINE column, it will transform the list in each row into separate rows. The resulting DataFrame will look like this:
```
   TRIP_ID  TAXI_ID  POLYLINE
0        1      123    [1,2]
0        1      123    [3,4]
0        1      123    [5,6]
1        2      456    [7,8]
1        2      456    [9,10]
```

In the mobility analytics context:

1. Each row in the original DataFrame represents one taxi trip
2. The 'POLYLINE' column contains a list of coordinate pairs representing the taxi's GPS points
3. explode() creates a new row for each coordinate pair while maintaining the other columns' values
4. This transformation is necessary to:
    - Process each GPS point individually
    - Create a proper trajectory object
    - Perform spatial analysis on individual points

It's similar to "unnesting" the GPS coordinates, making it easier to work with individual points in the trajectory.
"""
new_df = df.explode('POLYLINE')
new_df['geometry'] = new_df['POLYLINE'].apply(Point)
new_df['running_number'] = new_df.groupby('TRIP_ID').cumcount()
new_df['datetime'] = new_df.apply(compute_datetime, axis=1)
# print the first 5 rows of the new dataframe
print(
    f"Interim df for creating trajectory collection using the geometry and datetime columns\n: {new_df.head()}")

# :                TRIP_ID   TAXI_ID   TIMESTAMP  MISSING_DATA                POLYLINE  geo_len                     geometry  running_number            datetime
# 0  1372636858620000589  20000589  1372636858         False  [-8.618643, 41.141412]       23  POINT (-8.618643 41.141412)               0 2013-07-01 02:00:58
# 0  1372636858620000589  20000589  1372636858         False  [-8.618499, 41.141376]       23  POINT (-8.618499 41.141376)               1 2013-07-01 02:01:13
# 0  1372636858620000589  20000589  1372636858         False   [-8.620326, 41.14251]       23   POINT (-8.620326 41.14251)               2 2013-07-01 02:01:28


# drop the POLYLINE, TIMESTAMP, and running_number columns
new_df.drop(columns=['POLYLINE', 'TIMESTAMP', 'running_number'], inplace=True)

# print the first 5 rows of the new dataframe
print(
    f"Exploded the POLYLINE column into separate rows\n: {new_df.head()}")
# :                TRIP_ID   TAXI_ID  MISSING_DATA  geo_len                     geometry            datetime
# 0  1372636858620000589  20000589         False       23  POINT (-8.618643 41.141412) 2013-07-01 02:00:58
# 0  1372636858620000589  20000589         False       23  POINT (-8.618499 41.141376) 2013-07-01 02:01:13

# Creating trajectory collection from
gdf = gpd.GeoDataFrame(new_df, crs=4326)
trajs = mpd.TrajectoryCollection(
    gdf, traj_id_col='TRIP_ID', obj_id_col='TAXI_ID', t='datetime')


cleaned = trajs.copy()
cleaned = mpd.OutlierCleaner(cleaned).clean(v_max=100, units=("km", "h"))
cleaned.add_speed(overwrite=True, units=('km', 'h'))


# Add h3 indices at resolution 8 (you can adjust this resolution as needed)
gdf['h3'] = gdf.geometry.apply(lambda p: h3.geo_to_h3(p.y, p.x, 10))

h3cells = gdf['h3'].unique().tolist()


def polygonise(hex_id): return Polygon(
    h3.h3_to_geo_boundary(hex_id, geo_json=True)
)


all_polys = gpd.GeoSeries(
    list(map(polygonise, h3cells)), index=h3cells,
    name='geometry', crs="EPSG:4326")

all_polys = all_polys.reset_index()


def get_sub_traj(x):
    results = []
    tmp = cleaned.clip(x[1])
    if len(tmp.trajectories) > 0:
        for jtraj in tmp.trajectories:
            results.append([x[0], jtraj])
    return results


my_values = list(all_polys.values)
res = p_umap(get_sub_traj, my_values)


def flatten(l):
    return [[item[0], item[1]] for sublist in l for item in sublist]


tt = pd.DataFrame(flatten(res), columns=['index', 'traj'])
print(tt.head())


tt = tt.rename(columns={'index': 'h3'}).reset_index()
tt['st_split'] = tt['traj'].apply(
    lambda x: mpd.TemporalSplitter(x).split(mode="hour").trajectories)
st_traj = tt.explode('st_split')
st_traj.dropna(inplace=True)


def get_end_day_hour(traj):
    try:
        t = traj.get_end_time()
    except:
        print(traj)
    return datetime(t.year, t.month, t.day, t.hour, 0, 0)


st_traj['t'] = st_traj['st_split'].progress_apply(
    lambda x: get_end_day_hour(x))
st_traj['duration'] = st_traj['st_split'].progress_apply(
    lambda x: x.get_duration())


agg_st_traj = st_traj.groupby(['h3', 't'], as_index=False)['duration'].sum()
agg_st_traj['duration'] = agg_st_traj['duration'].apply(
    lambda x: x.total_seconds())

agg_st_traj['geometry'] = agg_st_traj['h3'].apply(
    lambda x: Polygon(h3.h3_to_geo_boundary(x, geo_json=True)))
print(agg_st_traj.head())

# write out the result to a geojson file
# convert the dataframe to a geodataframe
gdf = gpd.GeoDataFrame(agg_st_traj, crs=4326)
gdf.to_file('taxi-trajectory/agg_st_traj.geojson', driver='GeoJSON')
