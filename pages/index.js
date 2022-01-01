import Head from 'next/head'
import Link from 'next/link'
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'

import WorkPage from '../components/WorkPage'
import Header from '../components/Header'

export default function Home() {
  return (
    <div>
      <Head>
        <title>Autobiography Of Jack Torrance</title>
        <meta name="description" content="The writing of Jack Torrance" />
      </Head>
      <div className="flex flex-col h-screen">
        <Header />
        <div className="flex-grow" id="container">
          <pre>{`The Autobiography Of Jack Torrance 

             A Novel

        By Jack Torrance
          `}</pre>
        </div>
        <div className="pb-20 text-sm text-center text-gray-800">
          <span className="text-gray-300">&lt;-</span>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <Link href="/1">
            <a className="text-blue-500">-&gt;</a>
          </Link>
          &nbsp;
        </div>
      </div>
    </div>
  )
}
