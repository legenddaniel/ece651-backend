import { Product } from './product';

export interface Recipe {
  id: number;
  name: string;
  description: string;
  image_url: string;
  category: string;
  ingredients_id: number[];
  ingredients_product: Product[];
  rating: number;
  total_reviews: number;
  details: any;
}
