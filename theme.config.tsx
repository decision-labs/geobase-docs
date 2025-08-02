import React from "react";
import GeobaseLogo from "./components/geobase-logo";

const config = {
	head: ({ title }) => {
		return (
			<>
				<meta name="description" content="Find documentation, guides, examples, and blueprints for Geobase.app" />
				<title>{title ? `${title} — Geobase Docs` : 'Geobase Docs'}</title>
				<link rel="icon" type="image/x-icon" href="https://geobase.app/favicon.ico" />
			</>
		)
	},
	color: {
		hue: {
			dark: 152,
			light: 152,
		},
	},
	logo: (
		<GeobaseLogo
			style={{
				width: "8rem",
				height: "auto",
			}}
			/>
	),
	project: {
		link: "https://github.com/decision-labs/geobase",
	},
	chat: {
		link: "https://geobase.app/discord",
	},
	docsRepositoryBase: "https://github.com/sabman/geobase-docs",
	defaultShowCopyCode: true,
	footer: {
		content: `Geobase.app © ${new Date().getFullYear()}`,
	},
	sidebar: {
		defaultMenuCollapseLevel: 1
	}
};

export default config;
