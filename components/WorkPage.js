import Link from 'next/link'
import { useEffect } from 'react'

const pages = [
  '',
  `All work and no play makes Jack a dull boy`,
  `All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy`,
  'ALL work and no Play makes jack a dull boy',
  'allworkandnoplaymakesjackadullboy',
  `all work
and no play
makes jack
a dull boy`,
  `aLL wORK aND nO pLAY mAKES jACK a dULL bOY`,
  `ALL WORK and NO PLAY MAKES jack A DULL boy
all WORK and no PLAY MAKES JACK A dull boy
all work AND no play MAKES JACK A DULL BOY
all WORK and no PLAY makes JACK A DULL boy
ALL work and NO PLAY MAKES JACK a DULL boy
ALL work AND no play makes JACK A dull boy`,
  `All work and no play makes Jack a dull boy
All work             makes Jack a dull boy
All work             makes Jack a dull boy
All work             makes Jack a dull boy
All work             makes Jack a dull boy
All work             makes Jack a dull boy
All work             makes Jack a dull boy`,
]

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

  useEffect(() => {
    const pageJumper = setTimeout(jumpPage, 10000)
  })

  var pageNav
  if (page === '1') {
    pageNav = (
      <>
        Page {baseNum}{' '}
        <Link href="/2">
          <a className="text-blue-500">-&gt;</a>
        </Link>
      </>
    )
  } else if (baseNum === 2) {
    pageNav = (
      <>
        <Link href="/">
          <a className="text-blue-500">&lt;-</a>
        </Link>{' '}
        Page {baseNum}{' '}
        <Link href={`/${baseNum + 1}`}>
          <a className="text-blue-500">-&gt;</a>
        </Link>
      </>
    )
  } else if (baseNum < pages.length - 1) {
    pageNav = (
      <>
        <Link href={`/${baseNum - 1}`}>
          <a className="text-blue-500">&lt;-</a>
        </Link>{' '}
        Page {baseNum}{' '}
        <Link href={`/${baseNum + 1}`}>
          <a className="text-blue-500">-&gt;</a>
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
        <div className="bg-gray-800 tiny text-right text-gray-400 pr-2">
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
        <div className="flex-grow" id="container">
          <pre>{pages[page]}</pre>
        </div>
        <div className="pb-4 text-xs text-center text-gray-800">{pageNav}</div>
      </div>
    </>
  )
}
