import { Component, Input, OnInit } from '@angular/core';
import { Recipe } from '../../../model/recipe';
import { CartService } from '../../../services/cart.service';

@Component({
  selector: 'app-recipe',
  templateUrl: './recipe-item.component.html',
  styleUrls: ['./recipe-item.component.css']
})
export class RecipeItemComponent {
  @Input() recipeItem!: Recipe;
  constructor(private cartService: CartService) {}
}
