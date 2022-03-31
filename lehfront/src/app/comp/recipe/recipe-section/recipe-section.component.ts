import { Component, OnInit } from '@angular/core';
import { Recipe } from '../../../model/recipe';
import { Product } from '../../../model/product';
import { RecipeService } from '../../../services/recipe.service';

@Component({
  selector: 'app-recipe-section',
  templateUrl: './recipe-section.component.html',
  styleUrls: ['./recipe-section.component.css']
})
export class RecipeSectionComponent implements OnInit {
  recipeList: Recipe[] = [];
  recipeSection: Recipe[] = [];
  constructor(private recipeService: RecipeService) {}

  ngOnInit(): void {
    this.loadRecipes();
  }
  loadRecipes() {
    this.recipeService.getRecipes().subscribe((recipes) => {
      this.recipeList = recipes;
      this.getRandomRecipe();
    });
  }
  getRndInteger(min: number, max: number) {
    return Math.floor(Math.random() * (max - min)) + min;
  }

  getRandomRecipe() {
    if (this.recipeList.length <= 4) this.recipeSection = this.recipeList;
//     let randomNumbers = new Array(4);
//     let i = Math.min(4,this.recipeList.length);
//     for (let i = 0; i < 4; i++) {
//       let num = this.getRndInteger(0, this.recipeList.length);
//       while (randomNumbers.includes(num)) {
//         num = this.getRndInteger(0, this.recipeList.length);
//       }
//       randomNumbers[i] = num;
//     }
//     for (let i = 0; i < 4; i++) {
//       this.recipeSection.push(this.recipeList[randomNumbers[i]]);
//     }
    else{
      let num = this.getRndInteger(1, this.recipeList.length-4);
      for (let i = 0; i < 4; i++) {
        this.recipeSection.push(this.recipeList[num+i]);
      }
      console.log(this.recipeSection);
    }
  }
}
