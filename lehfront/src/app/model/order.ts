import { Product } from './product';

export interface OrderItem {
  id: number;
  productId: number;
  qty: number;
  product: Product;
  orderTime: Date;
  deliverTime: Date;
}
