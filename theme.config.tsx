import React from "react";
import { DocsThemeConfig } from "nextra-theme-docs";
import GeobaseLogo from "./components/geobase-logo";

const config: DocsThemeConfig = {
	useNextSeoProps() {
		return {
			titleTemplate: "%s — Geobase Docs",
			description: "Find documentation, guides, examples, and blueprints for Geobase.app",
		};
	},
	head: <link rel="icon" type="image/x-icon" href="https://geobase.app/favicon.ico" />,
	primaryHue: {
		dark: 152,
		light: 152,
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
		link: "https://discord.com",
	},
	docsRepositoryBase: "https://github.com/decision-labs/geobase-docs",
	footer: {
		text: `Geobase.app © ${new Date().getFullYear()}`,
	},
};

export default config;
