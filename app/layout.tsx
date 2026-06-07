import type { Metadata } from 'next'
import type { ReactNode } from 'react'
import { Footer, Layout, Navbar } from 'nextra-theme-docs'
import { Head } from 'nextra/components'
import { getPageMap } from 'nextra/page-map'
import GeobaseLogo from '../components/geobase-logo'
import 'nextra-theme-docs/style.css'

export const metadata: Metadata = {
  description:
    'Find documentation, guides, examples, and blueprints for Geobase.app',
  icons: {
    icon: 'https://geobase.app/favicon.ico',
  },
  title: {
    default: 'Geobase Docs',
    template: '%s — Geobase Docs',
  },
}

const navbar = (
  <Navbar
    logo={
      <GeobaseLogo
        style={{
          width: '8rem',
          height: 'auto',
        }}
      />
    }
    projectLink="https://github.com/decision-labs/geobase-docs"
    chatLink="https://geobase.app/discord"
  />
)

export default async function RootLayout({
  children,
}: {
  children: ReactNode
}) {
  const pageMap = await getPageMap()

  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head color={{ hue: 152 }} />
      <body>
        <Layout
          navbar={navbar}
          footer={<Footer>Geobase.app © {new Date().getFullYear()}</Footer>}
          pageMap={pageMap}
          docsRepositoryBase="https://github.com/decision-labs/geobase-docs/tree/main"
          sidebar={{ defaultMenuCollapseLevel: 1 }}
        >
          {children}
        </Layout>
      </body>
    </html>
  )
}
