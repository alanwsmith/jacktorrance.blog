import Link from 'next/link'
import { useEffect } from 'react'
import { pages } from './Pages'
import Header from './Header'

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
          <a className="text-blue-700">Cover</a>
        </Link>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <Link href={`/${baseNum - 1}`}>
          <a className="text-blue-700">&lt;-</a>
        </Link>
        {pageDisplay}
        <Link href={`/${baseNum + 1}`}>
          <a className="text-blue-700">-&gt;</a>
        </Link>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <Link href={`/${Math.floor(Math.random() * (pages.length - 2)) + 1}`}>
          <a className="text-blue-700">Random</a>
        </Link>
      </>
    )
  } else {
    let pageDisplay = `\u00A0\u00A0Page\u00A0\u00A0${baseNum}\u00A0\u00A0`
    if (baseNum > 9) {
      pageDisplay = `\u00A0\u00A0Page\u00A0${baseNum}\u00A0\u00A0`
    }
    pageNav = (
      <>
        <Link href="/">
          <a className="text-blue-700">Cover</a>
        </Link>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <Link href={`/${baseNum - 1}`}>
          <a className="text-blue-700">&lt;-</a>
        </Link>
        {pageDisplay}
        <span className="text-gray-300">-&gt;</span> &nbsp;&nbsp;&nbsp;
        <Link href={`/${Math.floor(Math.random() * (pages.length - 2)) + 1}`}>
          <a className="text-blue-700">Random</a>
        </Link>
      </>
    )
  }

  const pageText =
    page > 666 ? '[ this space intentionally left blank ]' : pages[page]

  return (
    <>
      <div className="flex flex-col h-screen">
        <Header />
        <div className="flex-grow pb-28" id="container">
          <pre className="text-md">{pageText}</pre>
        </div>
        <div className="pb-20 text-sm text-center text-gray-800">{pageNav}</div>
      </div>
    </>
  )
}
