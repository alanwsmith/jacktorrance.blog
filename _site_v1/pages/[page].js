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
        <title>Autobiography Of Jack Torrance</title>
        <meta name="description" content="The writing of Jack Torrance" />
      </Head>
      <WorkPage page={page} />
    </div>
  )
}
