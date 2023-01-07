import React from 'react'
import { Link } from 'react-router-dom'
export default function ProductDetails() {
    return (
        <div className=''>
            <section className='mb-10'>
                <div className="relative max-w-screen-xl px-4 py-8 mx-auto">

                    <div className="grid items-start grid-cols-1 gap-8 md:grid-cols-2">
                        <div className="grid grid-cols-2 gap-4 md:grid-cols-1">
                            <div className="grid grid-cols-2 gap-4 lg:mt-4">
                                <img
                                    alt="Les Paul"
                                    src="https://images.unsplash.com/photo-1456948927036-ad533e53865c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
                                    className="object-cover w-full aspect-square rounded-xl"
                                />

                                <img
                                    alt="Les Paul"
                                    src="https://images.unsplash.com/photo-1456948927036-ad533e53865c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
                                    className="object-cover w-full aspect-square rounded-xl"
                                />

                                <img
                                    alt="Les Paul"
                                    src="https://images.unsplash.com/photo-1456948927036-ad533e53865c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
                                    className="object-cover w-full aspect-square rounded-xl"
                                />

                                <img
                                    alt="Les Paul"
                                    src="https://images.unsplash.com/photo-1456948927036-ad533e53865c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
                                    className="object-cover w-full aspect-square rounded-xl"
                                />
                            </div>
                        </div>

                        <div className="sticky top-0">
                            <strong
                                class="rounded-full border border-[#6353C6] bg-gray-100 px-3 py-0.5 text-xs font-medium tracking-wide text-[#6353C6]"
                            >
                                Product Type
                            </strong>
                            <div className="flex justify-between mt-8">
                                <div className="max-w-[35ch]">
                                    <h1 className="text-2xl font-bold">
                                        Fun Product That Does Something Cool
                                    </h1>

                                    <p className="mt-0.5 text-sm">Highest Rated Product</p>

                                    <div className="mt-2 -ml-0.5 flex">
                                        <svg
                                            className="w-5 h-5 text-yellow-400"
                                            xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 0 20 20"
                                            fill="currentColor"
                                        >
                                            <path
                                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                                            />
                                        </svg>

                                        <svg
                                            className="w-5 h-5 text-yellow-400"
                                            xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 0 20 20"
                                            fill="currentColor"
                                        >
                                            <path
                                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                                            />
                                        </svg>

                                        <svg
                                            className="w-5 h-5 text-yellow-400"
                                            xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 0 20 20"
                                            fill="currentColor"
                                        >
                                            <path
                                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                                            />
                                        </svg>

                                        <svg
                                            className="w-5 h-5 text-yellow-400"
                                            xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 0 20 20"
                                            fill="currentColor"
                                        >
                                            <path
                                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                                            />
                                        </svg>

                                        <svg
                                            className="w-5 h-5 text-gray-200"
                                            xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 0 20 20"
                                            fill="currentColor"
                                        >
                                            <path
                                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                                            />
                                        </svg>
                                    </div>
                                </div>

                                <p className="text-lg font-bold">$119.99</p>
                            </div>

                            <details
                                className="group relative mt-4 [&_summary::-webkit-details-marker]:hidden"
                            >
                                <summary className="block">
                                    <div>
                                        <div className="prose max-w-none group-open:hidden">
                                            <p>
                                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa
                                                veniam dicta beatae eos ex error culpa delectus rem tenetur,
                                                architecto quam nesciunt, dolor veritatis nisi minus
                                                inventore, rerum at recusandae?
                                            </p>
                                        </div>

                                        <span
                                            className="mt-4 text-sm font-medium underline cursor-pointer group-open:absolute group-open:bottom-0 group-open:left-0 group-open:mt-0"
                                        >
                                            Read More
                                        </span>
                                    </div>
                                </summary>

                                <div className="pb-6 prose max-w-none">
                                    <p>
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa
                                        veniam dicta beatae eos ex error culpa delectus rem tenetur,
                                        architecto quam nesciunt, dolor veritatis nisi minus inventore,
                                        rerum at recusandae?
                                    </p>

                                    <p>
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat
                                        nam sapiente nobis ea veritatis error consequatur nisi
                                        exercitationem iure laudantium culpa, animi temporibus non! Maxime
                                        et quisquam amet. A, deserunt!
                                    </p>
                                </div>
                            </details>

                            <div className="mt-8">
                                <fieldset>
                                    <legend className="mb-1 text-sm font-medium">Color</legend>

                                    <div className="flow-root">
                                        <div className="-m-0.5 flex flex-wrap">
                                            <label htmlFor="color_tt" className="cursor-pointer p-0.5">
                                                <input
                                                    type="radio"
                                                    name="color"
                                                    id="color_tt"
                                                    className="sr-only peer"
                                                />

                                                <span
                                                    className="inline-block px-3 py-1 text-xs font-medium border rounded-full group peer-checked:bg-[#6353C6] peer-checked:text-white"
                                                >
                                                    Red
                                                </span>
                                            </label>

                                            <label htmlFor="color_fr" className="cursor-pointer p-0.5">
                                                <input
                                                    type="radio"
                                                    name="color"
                                                    id="color_fr"
                                                    className="sr-only peer"
                                                />

                                                <span
                                                    className="inline-block px-3 py-1 text-xs font-medium border rounded-full group peer-checked:bg-[#6353C6] peer-checked:text-white"
                                                >
                                                    Green
                                                </span>
                                            </label>

                                            <label htmlFor="color_cb" className="cursor-pointer p-0.5">
                                                <input
                                                    type="radio"
                                                    name="color"
                                                    id="color_cb"
                                                    className="sr-only peer"
                                                />

                                                <span
                                                    className="inline-block px-3 py-1 text-xs font-medium border rounded-full group peer-checked:bg-[#6353C6] peer-checked:text-white"
                                                >
                                                    Blue
                                                </span>
                                            </label>
                                        </div>
                                    </div>
                                </fieldset>
                                <fieldset class="mt-4">
                                    <legend class="mb-1 text-sm font-medium">Size</legend>

                                    <div class="flow-root">
                                        <div class="-m-0.5 flex flex-wrap">
                                            <label for="size_xs" class="cursor-pointer p-0.5">
                                                <input
                                                    type="radio"
                                                    name="size"
                                                    id="size_xs"
                                                    class="sr-only peer"
                                                />

                                                <span
                                                    class="inline-flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full group peer-checked:bg-[#6353C6] peer-checked:text-white"
                                                >
                                                    XS
                                                </span>
                                            </label>

                                            <label for="size_s" class="cursor-pointer p-0.5">
                                                <input
                                                    type="radio"
                                                    name="size"
                                                    id="size_s"
                                                    class="sr-only peer"
                                                />

                                                <span
                                                    class="inline-flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full group peer-checked:bg-[#6353C6] peer-checked:text-white"
                                                >
                                                    S
                                                </span>
                                            </label>

                                            <label for="size_m" class="cursor-pointer p-0.5">
                                                <input
                                                    type="radio"
                                                    name="size"
                                                    id="size_m"
                                                    class="sr-only peer"
                                                />

                                                <span
                                                    class="inline-flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full group peer-checked:bg-[#6353C6] peer-checked:text-white"
                                                >
                                                    M
                                                </span>
                                            </label>

                                            <label for="size_l" class="cursor-pointer p-0.5">
                                                <input
                                                    type="radio"
                                                    name="size"
                                                    id="size_l"
                                                    class="sr-only peer"
                                                />

                                                <span
                                                    class="inline-flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full group peer-checked:bg-[#6353C6] peer-checked:text-white"
                                                >
                                                    L
                                                </span>
                                            </label>

                                            <label for="size_xl" class="cursor-pointer p-0.5">
                                                <input
                                                    type="radio"
                                                    name="size"
                                                    id="size_xl"
                                                    class="sr-only peer"
                                                />

                                                <span
                                                    class="inline-flex items-center justify-center w-8 h-8 text-xs font-medium border rounded-full group peer-checked:bg-[#6353C6] peer-checked:text-white"
                                                >
                                                    XL
                                                </span>
                                            </label>
                                        </div>
                                    </div>
                                </fieldset>

                                <div className="flex mt-8 items-center">

                                    <Link
                                        to='/product-details'
                                        className="block px-5 py-3 ml-3 text-xs font-medium text-white bg-[#6353C6] rounded"
                                    >
                                        Product Link
                                    </Link>

                                    <button
                                        className="block px-5 py-2 text-sm font-medium transition  bg-white text-[#6353C6] border-2 border-[#6353C6] rounded hover:scale-105 ml-2"
                                    >
                                        Report
                                    </button>

                                    <button
                                        className="block px-5 py-2 text-sm font-medium transition  bg-white text-[#6353C6] border-2 border-[#6353C6] rounded hover:scale-105 ml-2"
                                    >
                                        Share
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    )
}
