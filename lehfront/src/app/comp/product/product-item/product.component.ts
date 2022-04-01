import { Component, Input, OnInit } from '@angular/core';
import { Product } from '../../../model/product';
import { CartService } from '../../../services/cart.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent {
  @Input() productItem!: Product;

  constructor(private cartService: CartService) {}
}
