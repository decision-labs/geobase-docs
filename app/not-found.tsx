import Link from 'next/link'

export default function NotFound() {
  return (
    <div className="x:flex x:flex-col x:justify-center x:items-center x:h-[calc(100dvh-var(--nextra-navbar-height))]">
      <h1 className="x:text-4xl x:font-bold">404: Page Not Found</h1>
      <Link href="/" className="x:mt-4 x:underline">
        Back to docs
      </Link>
    </div>
  )
}
