import Head from 'next/head'
import Link from 'next/link'
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'

export default function Home() {
  const [pageNum, setPageNum] = useState(1)
  const router = useRouter()

  const pages = [
    '',
    `all work and no play makes jack a dull boy
all work and no play makes jack a dull boy
all work and no play makes jack a dull boy
all work and no play makes jack a dull boy`,
    'ALL work and no Play makes jack a dull boy',
  ]

  useEffect(() => {
    if (!router.isReady) return
    if (router.query['page']) {
      const page = router.query['page']
      setPageNum(router.query['page'])
    }
  }, [router.isReady])

  return (
    <div>
      <Head>
        <title>A Jack Torrance Experience</title>
        <meta name="description" content="The writing of Jack Torrance" />
      </Head>

      <div className="flex flex-col h-screen">
        <div className="flex-grow" id="container">
          <pre>{pages[pageNum]}</pre>
        </div>
        <div>
          <a href="/?page=2">Page 2</a>
        </div>
        <div className="text-xs text-right">This is the footer</div>
      </div>
    </div>
  )
}
