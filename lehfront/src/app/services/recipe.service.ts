import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, Observable } from 'rxjs';
import { Recipe } from '../model/recipe';
import { recipesUrl } from 'src/app/config/api';

@Injectable({
  providedIn: 'root'
})
export class RecipeService {
  getRecipe(id: number): Observable<Recipe[]> {
    return this.http.get<Recipe[]>(recipesUrl + '?id=' + id);
  }

  constructor(private http: HttpClient) {}

  getRecipes(): Observable<Recipe[]> {
    return this.http.get<Recipe[]>(recipesUrl);
  }

  getRecipeByName(name: string): Observable<Recipe[]> {
    return this.http.get<Recipe[]>(recipesUrl + '?name=' + name);
  }
}
