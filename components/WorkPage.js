import Link from 'next/link'
import { useEffect } from 'react'
import { pages } from './Pages'

export default function WorkPage({ page }) {
  const baseNum = parseInt(page, 10)

  function jumpPage() {
    var pageToJumpTo = Math.floor(Math.random() * pages.length)
    if (pageToJumpTo === 0) {
      pageToJumpTo = 1
    }
    if (pageToJumpTo === baseNum) {
      pageToJumpTo = 2
      if (baseNum === 2) {
        pageToJumpTo = 1
      }
    }
    if (window) {
      window.location.href = `/${pageToJumpTo}`
    }
  }

  var pageNav
  if (baseNum === 1) {
    let pageDisplay = `\u00A0\u00A0Page\u00A0\u00A0${baseNum}\u00A0\u00A0`
    pageNav = (
      <>
        <Link href="/">
          <a className="text-blue-700">Cover</a>
        </Link>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <Link href="/">
          <a className="text-blue-700">&lt;-</a>
        </Link>
        {pageDisplay}
        <Link href="/2">
          <a className="text-blue-700">-&gt;</a>
        </Link>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <Link href={`/${Math.floor(Math.random() * (pages.length - 2)) + 1}`}>
          <a className="text-blue-700">Random</a>
        </Link>
      </>
    )
  } else if (baseNum < pages.length - 1) {
    let pageDisplay = `\u00A0\u00A0Page\u00A0\u00A0${baseNum}\u00A0\u00A0`
    if (baseNum > 9) {
      pageDisplay = `\u00A0\u00A0Page\u00A0${baseNum}\u00A0\u00A0`
    }

    pageNav = (
      <>
        <Link href="/">
          <a>Cover</a>
        </Link>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <Link href={`/${baseNum - 1}`}>
          <a className="text-blue-500">&lt;-</a>
        </Link>
        {pageDisplay}
        <Link href={`/${baseNum + 1}`}>
          <a className="text-blue-500">-&gt;</a>
        </Link>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <Link href={`/${Math.floor(Math.random() * (pages.length - 2)) + 1}`}>
          <a>Random</a>
        </Link>
      </>
    )
  } else {
    pageNav = (
      <>
        <Link href={`/${baseNum - 1}`}>
          <a className="text-blue-500">&lt;-</a>
        </Link>{' '}
        Page {baseNum}
      </>
    )
  }

  return (
    <>
      <div className="flex flex-col h-screen">
        <div className="bg-gray-800 text-sm text-right text-gray-400 pr-2">
          From{' '}
          <a className="text-blue-400" href="https://twitter.com/TheIdOfAlan">
            Alan W. Smith
          </a>{' '}
          (who has a{' '}
          <a
            className="text-blue-400"
            href="https://www.alanwsmith.com/the-pod-of-alan"
          >
            podcast
          </a>
          ) for{' '}
          <a className="text-blue-400" href="https://dusty.domains/">
            Dusty Domains 2021
          </a>
        </div>
        <div className="flex-grow pb-28" id="container">
          <pre className="text-md">{pages[page]}</pre>
        </div>
        <div className="pb-20 text-sm text-center text-gray-800">{pageNav}</div>
      </div>
    </>
  )
}
