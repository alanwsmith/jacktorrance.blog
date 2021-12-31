export default function Header() {
  return (
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
  )
}
