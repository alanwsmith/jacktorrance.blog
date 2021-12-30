import Head from 'next/head'
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'

export default function Home() {
  const [pageNum, setPageNum] = useState(1)
  const router = useRouter()

  useEffect(() => {
    if (!router.isReady) return
    const page = router.query['page']
    setPageNum(router.query['page'])
  }, [router.isReady])

  return (
    <div>
      <Head>
        <title>A Jack Torrance Experience</title>
        <meta name="description" content="The writing of Jack Torrance" />
      </Head>

      <div className="flex flex-col h-screen">
        <div className="flex-grow" id="container">
          <p>all work and no play makes jack a dull boy</p>
          <p>Page: {pageNum}</p>
        </div>
        <div className="text-xs text-right">This is the footer</div>
      </div>
    </div>
  )
}
