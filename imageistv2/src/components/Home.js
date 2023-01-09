import React from 'react'
import SearchIcon from '../assets/SearchIcon.png'

import {createContext, useContext,useState,useEffect} from 'react';
import { q } from '../App'
import {useNavigate} from 'react-router-dom'

export default function Home() {
    const navigate=useNavigate();
const [input,setInput]=useState();
  const {query,setQuery}=useContext(q);
  const inputHandle=(e)=>{
    
    console.log(query);
    setInput(e.target.value);
    setQuery(input);
  }
  const search=(e)=>{
    setQuery(input);
    if (query !='all'){
    navigate('/products');
    }
  }
    return (
        <div className='overflow-y-hidden'>            
            <div className="flex justify-center mt-[30vh] h-[75px] items-center my-1">
                {/* Search Row */}
                <div className="flex items-center p-2 bg-white rounded-[16px] border border-[#8978F1]">
                    <div className='h-[65px] bg-white flex flex-col justify-center mr-2'>
                        <img src={SearchIcon} className=' bg-white' alt="" srcSet="" />
                    </div>
                    <input value={input} onChange={inputHandle} type="search" className='form-control sm:w-full md:w-[600px] h-[65px]  p-1 placeholder:text-xl placeholder:opacity-50 border-none ocus:bg-white  focus:ring-0' placeholder='Search Here' />
                    <div className='h-[65px] bg-white flex flex-col justify-center'>
                        <button className='bg-[#6353C6] text-white rounded-[15px] px-5 py-2 font-bold text-2xl' onClick={search}>Search</button>
                    </div>
                </div>                
            </div>
            <h2 className='text-2xl underline text-center mt-4 hover:cursor-pointer'>Upload Image</h2>
        </div>
    )
}
