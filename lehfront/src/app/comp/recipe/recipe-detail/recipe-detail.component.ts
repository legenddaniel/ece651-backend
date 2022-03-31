import { Component, Input, OnInit } from '@angular/core';
import { Recipe } from '../../../model/recipe';
import { Product } from '../../../model/product';
import { CartService } from '../../../services/cart.service';
import { ActivatedRoute, Params } from '@angular/router';
import { RecipeService } from '../../../services/recipe.service';
import { UserService } from '../../../services/user.service';

@Component({
  selector: 'app-recipe-detail',
  templateUrl: './recipe-detail.component.html',
  styleUrls: ['./recipe-detail.component.css']
})
export class RecipeDetailComponent implements OnInit {
  recipeItem!: Recipe;
  cartAns: any;
  ifLogin = false;
  constructor(
    private cartService: CartService,
    private routeInfo: ActivatedRoute,
    private recipeService: RecipeService,
    private userService: UserService,
  ) {}

  ngOnInit(): void {
    const recipeId = this.routeInfo.snapshot.paramMap.get('id');
    console.log(recipeId);
    this.recipeService
      .getRecipe(Number(recipeId))
      .subscribe((res) => {this.recipeItem = res[0];console.log(this.recipeItem);});
    this.ifLogin = this.userService.getIfLogin();
  }

  handleAddAllToCart() {
    console.log(this.recipeItem);
    let arr = this.recipeItem.ingredients_id.map((id) => {
      return { product_id: id, quantity: 1 };
    });
    console.log('Add All to arr');
    console.log(arr);
    this.cartService.addProductsToCart(arr).subscribe((res) => {
      this.cartAns = res;
    });
    if(this.cartAns != undefined)
      this.judgeCartAns();
    console.log('adding product to cart');
  }

  judgeCartAns(){
    if (this.cartAns.length > 0) {
        alert('Successfully added to cart');
        return true;
      } else {
        alert('Sorry cannot add ingredients to kart');
        return false;
      }
  }
}
