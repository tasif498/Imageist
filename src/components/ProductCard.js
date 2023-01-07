import React from 'react'
import { Link } from 'react-router-dom'
export default function ProductCard() {
  return (
    <div className="relative block overflow-hidden group">
      <button
        className="absolute right-4 top-4 z-10 rounded-full bg-white p-1.5 text-gray-900 transition hover:text-gray-900/75"
      >
        <span className="sr-only">Wishlist</span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth="1.5"
          stroke="currentColor"
          className="w-4 h-4"
        >
          <path
            strokeLinecap="round"
            stroke-linejoin="round"
            d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
          />
        </svg>
      </button>

      <img
        src="https://images.unsplash.com/photo-1599481238640-4c1288750d7a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2664&q=80"
        alt=""
        className="object-cover w-full h-64 transition duration-500 group-hover:scale-105 sm:h-56"
      />

      <div className="relative p-6 bg-white border border-gray-100">
        <span
          className="whitespace-nowrap bg-[#6353C6] text-white px-3 py-1.5 text-xs font-medium rounded-lg"
        >
          New
        </span>

        <h3 className="mt-4 text-lg font-medium text-gray-900">Robot Toy</h3>

        <p className="mt-1.5 text-sm text-gray-700">$14.99</p>

        <Link to='/product-details'>
          <button
            className="block w-full p-4 text-sm font-medium transition bg-[#6353C6] text-white rounded-lg hover:scale-105 mt-3"
          >
            View Details
          </button>
        </Link>       
      </div>
    </div>

  )
}
