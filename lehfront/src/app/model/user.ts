import { CartItem } from './cart';
import { Product } from './product';
import { Recipe } from './recipe';

export interface User {
  // attributes
  id: string;
  token: string;
  username: string;
  email: string;
  credit_card: string;
  shipping_address: string;

  // date
  last_login: Date;
  date_joined: Date;
  expiry: Date;

  // Types
  is_active: boolean;
  is_staff: boolean;
  is_superuser: boolean;

  // Collections
  cart_items: CartItem[];
  orders: CartItem[];
  fav_recipes: any[];
  groups: any[];
  user_permissions: any[];
}
