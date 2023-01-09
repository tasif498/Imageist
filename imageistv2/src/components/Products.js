import React from 'react'
import ProductCard from './ProductCard'

import {createContext, useContext,useState,useEffect} from 'react';
import { q } from '../App'
export default function Products() {

    const {query,setQuery}=useContext(q);
    return (
        <div>
            <div className='max-w-screen-4xl px-4 sm:px-6 lg:px-8 my-3 py-4'>
                {/* Pagination */}
                <div className='flex justify-between my-5 items-center'>
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
                
                </div>

            </div>
        </div>
    )
}
