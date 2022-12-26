import React from 'react'
import './App.css';
import './product.css';
import img1 from '../cc.jpg';
import img2 from '../cc1.jpg';
function Product() {
    return (
        <span>
            <div class="row">
                <div class="col-md-3 col-sm-3">
                    <div class="product-grid">
                        <div class="product-image">
                            <a href="#" class="image">
                                <img class="pic-1" src={img1} />
                                <img class="pic-2" src={img2} />
                            </a>
                            <a href="#" class="product-like-icon"><i class="far fa-heart"></i></a>
                            <ul class="product-links">
                                <li><a href="#"><i class="fa fa-eye"></i></a></li>
                                <li><a href="#"><i class="fa fa-random"></i></a></li>
                                <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                            </ul>
                        </div>
                        <div class="product-content">
                            <h3 class="title"><a href="#">Men's Blazer</a></h3>
                            <div class="price">Rs.6500.00</div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-3 col-sm-6">
                    <div class="product-grid">
                        <div class="product-image">
                            <a href="#" class="image">
                                <img class="pic-1" src={img1} />
                                <img class="pic-2" src={img2} />
                            </a>
                            <a href="#" class="product-like-icon"><i class="far fa-heart"></i></a>
                            <ul class="product-links">
                                <li><a href="#"><i class="fa fa-eye"></i></a></li>
                                <li><a href="#"><i class="fa fa-random"></i></a></li>
                                <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                            </ul>
                        </div>
                        <div class="product-content">
                            <h3 class="title"><a href="#">Women's Top</a></h3>
                            <div class="price">Rs.4000.00</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-sm-6">
                    <div class="product-grid">
                        <div class="product-image">
                            <a href="#" class="image">
                                <img class="pic-1" src={img1} />
                                <img class="pic-2" src={img2} />
                            </a>
                            <a href="#" class="product-like-icon"><i class="far fa-heart"></i></a>
                            <ul class="product-links">
                                <li><a href="#"><i class="fa fa-eye"></i></a></li>
                                <li><a href="#"><i class="fa fa-random"></i></a></li>
                                <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                            </ul>
                        </div>
                        <div class="product-content">
                            <h3 class="title"><a href="#">Women's Top</a></h3>
                            <div class="price">Rs.4500.00</div>
                        </div>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6">
                    <div class="product-grid">
                        <div class="product-image">
                            <a href="#" class="image">
                                <img class="pic-1" src={img1} />
                                <img class="pic-2" src={img2} />
                            </a>
                            <a href="#" class="product-like-icon"><i class="far fa-heart"></i></a>
                            <ul class="product-links">
                                <li><a href="#"><i class="fa fa-eye"></i></a></li>
                                <li><a href="#"><i class="fa fa-random"></i></a></li>
                                <li><a href="#"><i class="fa fa-shopping-cart"></i></a></li>
                            </ul>
                        </div>
                        <div class="product-content">
                            <h3 class="title"><a href="#">Women's Top</a></h3>
                            <div class="price">Rs.900.00</div>
                        </div>
                    </div>
                </div>
        
        </span>
    );
}
export default Product;
