import Head from 'next/head'
import Link from 'next/link'
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'

import WorkPage from '../components/WorkPage'

export default function Home() {
  return (
    <div>
      <Head>
        <title>A Jack Torrance Experience</title>
        <meta name="description" content="The writing of Jack Torrance" />
      </Head>
      <WorkPage page="1" />
    </div>
  )
}
