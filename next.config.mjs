import nextra from 'nextra'
import { fileURLToPath } from 'url'

const appRoot = fileURLToPath(new URL('.', import.meta.url))

const withNextra = nextra({
  defaultShowCopyCode: true,
})

export default withNextra({
  reactStrictMode: true,
  outputFileTracingRoot: appRoot,
})
