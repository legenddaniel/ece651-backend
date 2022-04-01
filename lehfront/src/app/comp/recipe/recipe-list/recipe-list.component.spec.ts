import {
  ComponentFixture,
  TestBed,
  fakeAsync,
  tick
} from '@angular/core/testing';
import { RecipeListComponent } from './recipe-list.component';
import { RecipeService } from '../../../services/recipe.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { Recipe } from '../../../model/recipe';
import { Observable, of } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';

describe('RecipeListComponent', () => {
  let component: RecipeListComponent;
  let fixture: ComponentFixture<RecipeListComponent>;
  let recipeService: RecipeService;
  let response: Recipe[];
  let el: DebugElement[];

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [RecipeListComponent],
      providers: [RecipeService],
      imports: [HttpClientTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RecipeListComponent);
    component = fixture.componentInstance;
    recipeService = TestBed.get(RecipeService);
    response = [
      {
        id: 1,
        name: 'test recipe1',
        description: 'recipe desc1',
        image_url:
          'https://www.rockrecipes.com/wp-content/uploads/2016/04/Mongolian-Beef-close-up.jpg',
        category: 'French',
        ingredients_id: [1, 2, 3, 4],
        ingredients_product: [],
        rating: 5,
        total_reviews: 94,
        details: ['aaa', 'bbb']
      },
      {
        id: 2,
        name: 'test recipe2',
        description: 'recipe desc2',
        image_url:
          'https://www.rockrecipes.com/wp-content/uploads/2016/04/Mongolian-Beef-close-up.jpg',
        category: 'French',
        ingredients_id: [1, 2, 3],
        ingredients_product: [],
        rating: 5,
        total_reviews: 90,
        details: ['aaa', 'ccc']
      }
    ];
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should get recipe list', fakeAsync(() => {
    spyOn(recipeService, 'getRecipes').and.returnValue(of<any[]>(response));
    component.loadRecipes();
    expect(component.recipeList).toBe(response);
    el = fixture.debugElement.queryAll(By.css('app-recipe'));
    expect(el).toBeTruthy();
  }));
});
