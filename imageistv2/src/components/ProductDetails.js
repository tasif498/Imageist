import React from 'react'
import { Link, Navigate } from 'react-router-dom'
import { SKU } from '../App'
import axios from "axios";
import {createContext, useContext,useState,useEffect} from 'react';
export default function ProductDetails() {
    
  const {product_sku,setSKU}=useContext(SKU);
    
  const [data, setData] = useState({});
  const reportPage=(link)=>{
    const encoded_link=encodeURIComponent(link);
    axios.get('http://127.0.0.1:8000/report/?l='+encoded_link).then(
        response => {
        console.log('Link has been reported');
        }
    ).catch(error=>{
        console.log('Link could not be reported')
    }
    )
  };

  useEffect(() => {
    // console.log("dfgh    :",product_sku)
    const encoded_product_sku=encodeURIComponent(product_sku.trim());
    axios.get('http://127.0.0.1:8000/search/?q='+encoded_product_sku)
      .then(response => {

        console.log(response.data);

        setData(response.data[0]);

        console.log('images    ;   ',data)

      })
      .catch(error => {
        console.error(error);
      });


  }, data);

    return (
        <div className=''>
            <section className='mb-10'>
                <div className="relative max-w-screen-xl px-4 py-8 mx-auto">

                    <div className="grid items-start grid-cols-1 gap-8 md:grid-cols-2">
                        <div className="grid grid-cols-2 gap-4 md:grid-cols-1">
                            <div className="grid grid-cols-2 gap-4 lg:mt-4">
                                <img
                                    alt="Les Paul"
                                    src={data.images}
                                    className="object-cover aspect-square rounded-xl"
                                />

                                <img
                                    alt="Les Paul"
                                    src={data.images}
                                    className="object-cover aspect-square rounded-xl"
                                />

                                <img
                                    alt="Les Paul"
                                    src={data.images}
                                    className="object-cover aspect-square rounded-xl"
                                />

                                <img
                                    alt="Les Paul"
                                    src={data.images}
                                    className="object-cover aspect-square rounded-xl"
                                />
                            </div>
                        </div>

                        <div className="sticky top-0">
                            <strong
                                class="rounded-full border border-[#6353C6] bg-gray-100 px-3 py-0.5 text-xs font-medium tracking-wide text-[#6353C6]"
                            >
                            {data.type}
                            </strong>
                            <div className="flex justify-between mt-8">
                                <div className="max-w-[35ch]">
                                    <h1 className="text-2xl font-bold">
                                        {data.title}
                                    </h1>

                                </div>

                                <p className="text-lg font-bold">{data.price}</p>
                            </div>

                            <details
                                className="group relative mt-4 [&_summary::-webkit-details-marker]:hidden"
                            >
                                <summary className="block">
                                    <div>
                                        <div className="prose max-w-none group-open:hidden">
                                            <p>
                                                {data.description}
                                            </p>
                                        </div>

                                    </div>
                                </summary>

                                <div className="pb-6 prose max-w-none">
                                    <p>
                                        {data.description}
                                    </p>
                                </div>
                            </details>

                            <div className="mt-8">
                                <fieldset>
                                    <legend className="mb-1 text-sm font-medium">Color</legend>

                                    <div className="flow-root">
                                        <div className="-m-0.5 flex flex-wrap">
                                            {data.colors}
                                        </div>
                                    </div>
                                </fieldset>
                                <fieldset class="mt-4">
                                    <legend class="mb-1 text-sm font-medium">Size</legend>

                                    <div class="flow-root">
                                        <div class="-m-0.5 flex flex-wrap">
                                            {data.sizes}
                                        </div>
                                    </div>
                                </fieldset>

                                <div className="flex mt-8 items-center">

                                    <a href={data.product_link}
                                        className="block px-5 py-3 ml-3 text-xs font-medium text-white bg-[#6353C6] rounded"
                                    >
                                        Product Link
                                    </a>

                                    <button onClick={reportPage(data.product_link)}
                                        className="block px-5 py-2 text-sm font-medium transition  bg-white text-[#6353C6] border-2 border-[#6353C6] rounded hover:scale-105 ml-2"
                                    >
                                        Report
                                    </button>

                                    <a
                                        className="block px-5 py-2 text-sm font-medium transition  bg-white text-[#6353C6] border-2 border-[#6353C6] rounded hover:scale-105 ml-2"
                                    >
                                        Share
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    )
}
