import { Component, OnInit } from '@angular/core';
import { Recipe } from '../../../model/recipe';
import { Product } from '../../../model/product';
import { RecipeService } from '../../../services/recipe.service';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent implements OnInit {
  recipeList: Recipe[] = [];
  wishlist: number[] = [];

  constructor(private recipeService: RecipeService) {}

  ngOnInit(): void {
    this.loadRecipes();
  }

  loadRecipes() {
    this.recipeService.getRecipes().subscribe((recipes) => {
      this.recipeList = recipes;
    });
  }
}
