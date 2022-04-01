import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map, Observable, of } from 'rxjs';
import { CartItem } from '../model/cart';
import { cartUrl } from '../config/api';
import { orderUrl } from '../config/api';
import { Product } from '../model/product';
import { ProductService } from './product.service';
import { UserService } from './user.service';
import { User } from '../model/user';
import { convertElementSourceSpanToLoc } from '@angular-eslint/template-parser/dist/template-parser/src/convert-source-span-to-loc';
import { sortAndDeduplicateDiagnostics } from 'typescript';
import { CheckoutOrder } from '../model/checkout';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  index = 5;
  user: User | null = null;
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(
    private http: HttpClient,
    private userService: UserService,
    private productService: ProductService
  ) {
    this.userService.getUser().subscribe((user) => {
      this.user = user;
      if (this.user != null) {
        this.httpOptions = {
          headers: new HttpHeaders({
            'Content-Type': 'application/json',
            Authorization: 'Token ' + this.user.token
          })
        };
      }
    });
  }

  getCartItems(): Observable<any> {
    if (!this.user) return of([]);
    console.log('getCartItems');
    console.log(this.user);
    console.log(this.httpOptions);
    this.httpOptions.headers.set('Authorization', 'token ' + this.user.token);
    return this.http.get<any>(cartUrl, this.httpOptions);
  }

  //add
  addProductToCart(product: Product, qty: number): Observable<any> {
    if (!this.user) return of([]); // TODO: catch error here
    console.log(this.httpOptions);
    this.httpOptions.headers.set('Authorization', 'token ' + this.user.token);
    return this.http.post(
      cartUrl,
      { product_id: product.id, quantity: qty },
      this.httpOptions
    );
  }

  addProductsToCart(
    li: { product_id: number; quantity: number }[]
  ): Observable<any> {
    if (!this.user) return of([]); // TODO: catch error here
    console.log(this.httpOptions);
    this.httpOptions.headers.set('Authorization', 'token ' + this.user.token);
    return this.http.post(cartUrl, li, this.httpOptions);
  }

  delProduct(id: number) {
    if (!this.user) return of([]); // TODO: catch error here
    console.log(this.httpOptions);
    this.httpOptions.headers.set('Authorization', 'token ' + this.user.token);
    return this.http.patch(
      cartUrl + id + '/',
      { quantity: 0 },
      this.httpOptions
    );
  }

  create_new_order(order_status: string, order: Array<CheckoutOrder>) {
    if (!this.user) return of([]); // TODO: catch error here
    console.log(this.httpOptions);
    console.log('status = ', order_status);
    console.log('order = ', order);
    let obj = { order_status, order };
    console.log('I am tring to post this to backend: ', obj);
    this.httpOptions.headers.set('Authorization', 'token ' + this.user.token);
    return this.http.post(
      orderUrl,
      { status: order_status, order_items: order },
      this.httpOptions
    );
  }
}
