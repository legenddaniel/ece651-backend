import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RecipeService } from '../../../services/recipe.service';
import { ProductService } from '../../../services/product.service';
import { Recipe } from '../../../model/recipe';
import { Product } from '../../../model/product';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  recipeCandidates: Recipe[] = [];
  productCandidates: Product[] = [];
  key!: string;

  constructor(
    private routeInfo: ActivatedRoute,
    private recipeService: RecipeService,
    private productService: ProductService
  ) {}

  ngOnInit(): void {
    this.routeInfo.paramMap.subscribe((word) => {
      const key = word.get('key') as string;
      this.key = key;
      this.init(key);
      this.initProduct(key);
    });
  }

  init(key: string) {
    this.recipeService
      .getRecipeByName(key)
      .subscribe((res) => (this.recipeCandidates = res));
  }
  initProduct(key: string) {
    this.productService
      .getProductByName(key)
      .subscribe((res) => (this.productCandidates = res));
  }
}
