import Link from 'next/link'

const pages = [
  '',
  `all work and no play makes jack a dull boy
all work and no play makes jack a dull boy
all work and no play makes jack a dull boy
all work and no play makes jack a dull boy`,
  'ALL work and no Play makes jack a dull boy',
  'allworkandnoplaymakesjackadullboy',
  `all work
and no play
makes jack
a dull boy`,
]

export default function WorkPage({ page }) {
  var pageNav
  const baseNum = parseInt(page, 10)
  if (page === '1') {
    pageNav = (
      <div className="text-center text-sm text-gray-400">
        Page {baseNum}{' '}
        <Link href="/2">
          <a className="text-blue-500">-&gt;</a>
        </Link>
      </div>
    )
  } else if (baseNum === 2) {
    pageNav = (
      <div className="text-center text-sm text-gray-400">
        <Link href="/">
          <a className="text-blue-500">&lt;-</a>
        </Link>{' '}
        Page {baseNum}{' '}
        <Link href={`/${baseNum + 1}`}>
          <a className="text-blue-500">-&gt;</a>
        </Link>
      </div>
    )
  } else if (baseNum < pages.length - 1) {
    pageNav = (
      <div className="text-center text-sm text-gray-400">
        <Link href={`/${baseNum - 1}`}>
          <a className="text-blue-500">&lt;-</a>
        </Link>{' '}
        Page {baseNum}{' '}
        <Link href={`/${baseNum + 1}`}>
          <a className="text-blue-500">-&gt;</a>
        </Link>
      </div>
    )
  } else {
    pageNav = (
      <div className="text-center text-sm text-gray-400">
        <Link href={`/${baseNum - 1}`}>
          <a className="text-blue-500">&lt;-</a>
        </Link>{' '}
        Page {baseNum}
      </div>
    )
  }

  return (
    <>
      <div className="flex flex-col h-screen">
        <div className="flex-grow" id="container">
          <pre>{pages[page]}</pre>
        </div>
        <div>{pageNav}</div>
        <div className="text-xs text-right">This is the footer</div>
      </div>
    </>
  )
}
