import Head from 'next/head'
import Link from 'next/link'
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'

import WorkPage from '../components/WorkPage'

export default function Home() {
  // const [pageNum, setPageNum] = useState(1)
  // const router = useRouter()

  // useEffect(() => {
  //   if (!router.isReady) return
  //   if (router.query['page']) {
  //     const page = router.query['page']
  //     setPageNum(router.query['page'])
  //   }
  // }, [router.isReady, router.query])

  return (
    <div>
      <Head>
        <title>A Jack Torrance Experience</title>
        <meta name="description" content="The writing of Jack Torrance" />
      </Head>

      <WorkPage page="1" />

      <div className="flex flex-col h-screen">
        <div className="flex-grow" id="container"></div>
        <div></div>
        <div className="text-xs text-right">This is the footer</div>
      </div>
    </div>
  )
}
