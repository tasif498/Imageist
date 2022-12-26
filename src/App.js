import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./component/Navbar";
import Home from "./component/pages/Home";
import Product from "./component/pages/product";
function App() {
  return (

     <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/home" element={<Home/>}>
          </Route>
          <Route path="/product" element={<Product/>}>
          </Route>
        </Routes>
        
        
      </div>
    </Router>
  );
}

export default App;
