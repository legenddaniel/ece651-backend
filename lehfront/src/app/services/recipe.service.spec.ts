import { TestBed, fakeAsync, tick } from '@angular/core/testing';
import { RecipeService } from './recipe.service';
import {
  HttpClientTestingModule,
  HttpTestingController
} from '@angular/common/http/testing';
import { HttpClient } from '@angular/common/http';
import { recipesUrl } from 'src/app/config/api';
import { Recipe } from '../model/recipe';

describe('RecipeService', () => {
  let service: RecipeService;
  let httpTestingController: HttpTestingController;
  let response: Recipe;
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(RecipeService);
    httpTestingController = TestBed.get(HttpTestingController);
    response = {
      id: 1,
      name: 'test recipe',
      description: 'recipe desc',
      image_url:
        'https://www.rockrecipes.com/wp-content/uploads/2016/04/Mongolian-Beef-close-up.jpg',
      category: 'French',
      ingredients_id: [1, 2, 3, 4],
      ingredients_product: [],
      rating: 5,
      total_reviews: 94,
      details: ['aaa', 'bbb']
    };
  });

  afterEach(() => {
    httpTestingController.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('get all recipes', fakeAsync(() => {
    service.getRecipes().subscribe((res) => {
      expect((res as any).id).toBe(response.id);
      expect((res as any).name).toBe(response.name);
      expect((res as any).description).toBe(response.description);
      expect((res as any).image_url).toBe(response.image_url);
      expect((res as any).ingredients_id).toBe(response.ingredients_id);
      expect((res as any).details).toBe(response.details);
    });
    const req = httpTestingController.expectOne(recipesUrl);
    expect(req.request.method).toEqual('GET');
    req.flush(response);
    tick();
  }));

  it('get recipe by id', fakeAsync(() => {
    service.getRecipe(response.id).subscribe((res) => {
      expect((res as any).id).toBe(response.id);
    });
    const req = httpTestingController.expectOne(
      recipesUrl + '?id=' + response.id
    );
    expect(req.request.method).toEqual('GET');
    req.flush(response);
    tick();
  }));

  it('get recipe by name', fakeAsync(() => {
    service.getRecipeByName(response.name).subscribe((res) => {
      console.log(res);
      expect((res as any).name).toBe(response.name);
    });
    const req = httpTestingController.expectOne(
      recipesUrl + '?name=' + response.name
    );
    expect(req.request.method).toEqual('GET');
    req.flush(response);
    tick();
  }));
});
