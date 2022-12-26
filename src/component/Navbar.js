import React, { useState } from "react";
import "./Navbar.css";
import img1 from './logo1.png';
const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="Navbar">
      <span className="nav-logo" ><img src={img1} alt="Imageist"height="45px" width="110"/></span>
      <div className={`nav-items ${isOpen && "open"}`}>
        <a href="/home">Home</a>
        <a href="/about">About</a>
        <a href="/product">Product</a>
        <a href="/contact">Contact</a>
        <button type="button" class="button">API</button>
      </div>
      <div
        className={`nav-toggle ${isOpen && "open"}`}
        onClick={() => setIsOpen(!isOpen)}
      >
        <div className="bar"></div>
      </div>
    </div>
    
  );

};
export default Navbar;
