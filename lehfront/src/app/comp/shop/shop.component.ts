import { Component, OnInit } from '@angular/core';
import { Product } from '../../model/product';
import { UserService } from '../../services/user.service';
import { CartItem } from '../../model/cart';
import { CartService } from '../../services/cart.service';

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.css']
})
export class ShopComponent {}
