import { Component, Input, OnInit } from '@angular/core';
import { Product } from '../../../model/product';
import { UserService } from '../../../services/user.service';
import { CartService } from '../../../services/cart.service';
import { ActivatedRoute, Params } from '@angular/router';
import { ProductService } from '../../../services/product.service';

@Component({
  selector: 'app-product-item-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {
  productItem!: Product;
  product_qty = 1;
  ifLogin = false;

  constructor(
    private cartService: CartService,
    private userService: UserService,
    private routeInfo: ActivatedRoute,
    private productService: ProductService
  ) {}

  ngOnInit(): void {
    const productId = this.routeInfo.snapshot.paramMap.get('id');
    this.productService
      .getProduct(Number(productId))
      .subscribe((product) => (this.productItem = product[0]));
    this.ifLogin = this.userService.getIfLogin();
  }

  addToKart() {
    console.log('addToKart triggered');
    console.log(this.product_qty);
    this.cartService
      .addProductToCart(this.productItem, this.product_qty)
      .subscribe((res) => {
        console.log('added to cart', res);
      });
  }
}
