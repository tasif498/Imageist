import React from 'react'
import ProductCard from './ProductCard'

export default function Products() {

    return (
        <div>
            <div className='max-w-screen-4xl px-4 sm:px-6 lg:px-8 my-3 py-4'>
                {/* Pagination */}
                <div className='flex justify-between my-5 items-center'>
                    <h2 className='font-bold text-sm'>
                        <span className='font-bold '>Showing 1 - 20 </span>
                        <span className='text-gray-600'> out of 2,356 Products</span>
                    </h2>
                    <select className="form-select text-sm form-select-lg mb-3 appearance-none block pr-24 py-2 text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-purple-600 focus:outline-none font-semibold">
                        <option value="">Sort By:</option>
                        <option value="Jeans">Jeans</option>
                        <option value="Pents">Pents</option>
                        <option value="Shirts">Shirts</option>
                        <option value="Coats">Coats</option>
                    </select>

                </div>
                <div className='flex flex-wrap gap-8 mt-10'>
                    <ProductCard />
                    <ProductCard />
                    <ProductCard />
                </div>

            </div>
        </div>
    )
}
