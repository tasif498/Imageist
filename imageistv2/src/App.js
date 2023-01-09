import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Components
import Home from './components/Home';
import Products from './components/Products';
import ProductDetails from './components/ProductDetails';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import ProductCard from './components/ProductCard';
import {createContext, useContext,useState} from 'react';


const SKU=createContext();
const q=createContext();


function App() {
  const [product_sku,setSKU]=useState("")
  const [query,setQuery]=useState('all')
  return (
    <SKU.Provider value={{product_sku,setSKU}}>
    <q.Provider value={{query,setQuery}}>
    <Router>
          <Navbar />
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/products' element={<Products />} />
            <Route path='/product-details' element={<ProductDetails />} />
            <Route path='/productscard' element={<ProductCard />} />
            
          </Routes>
          <Footer />
        </Router>
        </q.Provider>
        </SKU.Provider>
  );
}

export default App;
export {SKU,q};