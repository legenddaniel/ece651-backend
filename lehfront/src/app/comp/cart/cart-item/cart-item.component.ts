import { Component, Input, OnInit } from '@angular/core';
import { CartItem } from '../../../model/cart';

@Component({
  selector: 'app-cart-item',
  templateUrl: './cart-item.component.html',
  styleUrls: ['./cart-item.component.css']
})
export class CartItemComponent {
  @Input() cartItem!: CartItem;
  constructor() {
    console.log();
  }
}
