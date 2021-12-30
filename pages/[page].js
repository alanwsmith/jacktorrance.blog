import Head from 'next/head'
import Link from 'next/link'
import { useRouter } from 'next/router'

import WorkPage from '../components/WorkPage'

export default function Home() {
  const router = useRouter()
  const { page } = router.query

  return (
    <div>
      <Head>
        <title>A Jack Torrance Experience</title>
        <meta name="description" content="The writing of Jack Torrance" />
      </Head>

      <div className="flex flex-col h-screen">
        <div className="flex-grow" id="container"></div>
        <WorkPage page={page} />
        <div className="text-xs text-right">This is the footer</div>
      </div>
    </div>
  )
}
