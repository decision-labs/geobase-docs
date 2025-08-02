# Oriented Object Detection

> **Task ID:** `oriented-object-detection`  
> **Library:** `@geobase-js/geoai`  
> **Purpose:** Detection of oriented objects in aerial and satellite imagery with rotational awareness

## Quick Start

```typescript
import { geoai } from "@geobase-js/geoai";

// Initialize the pipeline
const orientedDetectionInstance = await geoai.pipeline(
  [
    {
      task: "oriented-object-detection",
      modelId: "geobase/gghl-oriented-object-detection", //optional
    },
  ],
  providerParams
);

// Run inference
const result = await orientedDetectionInstance.inference({
  inputs: { polygon: myPolygon },
  mapSourceParams: { zoomLevel: 18 },
  postProcessingParams: { 
    conf_thres: 0.5,
    iou_thres: 0.45,
    multi_label: true
  },
});

console.log(`Found ${result.detections.features.length} oriented objects`);
```

## Available Models

| Model ID | Description | Best Use Case |
|----------|-------------|---------------|
| [geobase/gghl-oriented-object-detection](https://huggingface.co/geobase/gghl-oriented-object-detection) | GGHL oriented object detection model | Aerial imagery analysis with rotational object detection |

## Capabilities

- ✅ **Oriented bounding boxes** - Detects objects with rotation and orientation
- ✅ **Multi-class detection** - 15 specialized object classes optimized for aerial imagery
- ✅ **High-resolution support** - Optimized for satellite and aerial imagery analysis
- ✅ **NMS post-processing** - Advanced Non-Maximum Suppression with configurable parameters
- ✅ **Confidence scoring** - Each detection includes confidence scores for quality filtering
- ✅ **Geospatial integration** - Native GeoJSON output with geographic coordinates
- ✅ **Pipeline chaining** - Compatible with other geospatial AI tasks

## Input Parameters

### Required Inputs

| Parameter | Type | Description |
|-----------|------|-------------|
| `polygon` | `GeoJSON.Feature<Polygon>` | Area of interest for oriented object detection |

### Post Processing Parameters (NMS Options)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `conf_thres` | `number` | `0.5` | Confidence threshold for detections (0-1) |
| `iou_thres` | `number` | `0.45` | IoU threshold for Non-Maximum Suppression |
| `multi_label` | `boolean` | `true` | Allow multiple labels per detection |
| `classes` | `number[]` | `undefined` | Filter specific class indices |
| `without_iouthres` | `boolean` | `false` | Skip IoU threshold filtering |

<!-- Todo : update the map source guide link -->
### Map Source Parameters
Follow this guide for mapSourceParameters 

## Output Format

```typescript
interface ObjectDetectionResults {
  detections: GeoJSON.FeatureCollection;
  geoRawImage: GeoRawImage;
}
```

### Detection Feature Properties

```typescript
interface DetectionProperties {
  score: string;        // Detection confidence (0-1)
  class_name: number;   // Object class name
}
```

## Detected Object Classes

| Class | Description | Typical Use Cases |
|-------|-------------|-------------------|
| `plane` | Aircraft and airplanes | Airport monitoring, aviation analysis |
| `baseball-diamond` | Baseball fields and diamonds | Sports facility mapping, land use analysis |
| `bridge` | Bridges and overpasses | Infrastructure inventory, transportation analysis |
| `ground-track-field` | Athletic tracks and fields | Sports facility detection, urban planning |
| `small-vehicle` | Cars and small vehicles | Traffic analysis, parking assessment |
| `large-vehicle` | Trucks and large vehicles | Commercial traffic monitoring, logistics |
| `ship` | Ships and maritime vessels | Port monitoring, maritime traffic analysis |
| `tennis-court` | Tennis courts | Sports facility mapping, recreational area analysis |
| `basketball-court` | Basketball courts | Sports infrastructure, urban planning |
| `storage-tank` | Industrial storage tanks | Industrial monitoring, facility management |
| `soccer-ball-field` | Soccer fields and pitches | Sports facility detection, land use planning |
| `roundabout` | Traffic roundabouts | Transportation infrastructure, traffic analysis |
| `harbor` | Harbors and ports | Maritime infrastructure, coastal analysis |
| `swimming-pool` | Swimming pools | Residential analysis, recreational facility mapping |
| `helicopter` | Helicopters | Aviation monitoring, emergency response analysis |

## Key Differences from Standard Object Detection

### Oriented Bounding Boxes
Unlike standard object detection that uses axis-aligned rectangles, oriented object detection provides:
- **Rotational awareness** - Objects detected with their actual orientation
- **Better fit** - Oriented boxes provide tighter bounds around rotated objects
- **Improved accuracy** - Reduced false positives from overlapping axis-aligned boxes

## Example Use Cases

### Transportation Analysis
```typescript
// Detect oriented vehicles and transportation infrastructure
const result = await orientedDetectionInstance.inference({
  inputs: { polygon: highwayIntersection },
  postProcessingParams: { 
    conf_thres: 0.6,
  },
});
```

## Performance Tips

### Optimization Strategies
- **Zoom level selection** - Use zoom level 16-19 for optimal detection accuracy
- **Confidence tuning** - Adjust `conf_thres` based on your accuracy requirements
- **Class filtering** - Use the `classes` parameter to focus on relevant object types
- **NMS tuning** - Adjust `iou_thres` for dense object scenarios

### Best Practices
- **Large areas** - Process large areas in smaller chunks for better performance
- **Multi-label detection** - Enable `multi_label` for complex scenes with overlapping objects
- **Quality filtering** - Use higher confidence thresholds for critical applications