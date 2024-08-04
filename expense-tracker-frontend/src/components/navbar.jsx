export default function Navbar() {
  return (<header>
    <nav className="flex justify-between items-center px-5 py-3">
      <img src="https://placehold.co/200x50" />
      <ul className="flex gap-x-3">
        <button className="bg-gray-300 px-5 py-2 rounded-lg hover:bg-gray-200">Login</button>
        <button className="bg-gray-300 px-5 py-2 rounded-lg hover:bg-gray-200">Register</button>
      </ul>
    </nav>
  </header>)
}
