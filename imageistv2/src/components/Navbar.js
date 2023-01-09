import React from 'react'
import Logo from '../assets/logo.png'
import { Link } from 'react-router-dom'
export default function Navbar() {
    return (
        <header aria-label="Site Header">
            <div className="mx-auto max-w-screen-4xl px-4 sm:px-6 lg:px-8">
                <div className="flex h-16 items-center justify-between">
                    <div className='w-3/12'>
                        <div className="md:flex md:items-center ">
                            <a className="block text-teal-600" href="/">
                                <span className="sr-only">Home</span>
                                <img src={Logo} alt="" srcSet="" className='' />
                            </a>
                        </div>
                    </div>
                    <div className='w-6/12'>
                        <div className="md:flex md:items-center flex-1 justify-center">
                            <nav aria-label="Site Nav" className="hidden md:block">
                                <ul className="flex items-center text-sm gap-16">
                                    <li>
                                        <Link
                                            className="transition hover:font-semibold text-base"
                                            to="/"
                                        >
                                            Home
                                        </Link>
                                    </li>
                                  

                                    <li>
                                        <Link
                                            className="transition hover:font-semibold text-base"
                                            to="/products"
                                        >
                                            Products
                                        </Link>
                                    </li>                                 
                                </ul>
                            </nav>
                        </div>
                    </div>
                    <div className='w-3/12 text-right'>
                        <button className='bg-[#6353C6] text-white rounded-[15px] px-10 py-2 text-lg font-semibold'>API</button>
                    </div>
                </div>
            </div>
        </header>

    )
}
