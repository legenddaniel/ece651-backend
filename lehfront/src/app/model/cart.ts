import { Product } from './product';

export interface CartItem {
  id: number;
  productId: number;
  qty: number;
  product?: Product;
}
