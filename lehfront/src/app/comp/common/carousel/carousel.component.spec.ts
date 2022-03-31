import { ComponentFixture, TestBed, fakeAsync, tick } from '@angular/core/testing';
import { RecipeService } from '../../../services/recipe.service';
import { Recipe } from '../../../model/recipe';
import { Observable, of } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { CarouselComponent } from './carousel.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { Router } from '@angular/router';

describe('CarouselComponent', () => {
  let component: CarouselComponent;
  let fixture: ComponentFixture<CarouselComponent>;
  let recipeService: RecipeService;
  let response: Recipe[];
  let el: DebugElement[];

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CarouselComponent],
      providers: [RecipeService],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CarouselComponent);
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

  //测试service getRecipe
  it('get information of recommended recipe', fakeAsync(() => {
     spyOn(recipeService, 'getRecipes').and.returnValue(of<any[]>(response));
     fixture = TestBed.createComponent(CarouselComponent);
     component = fixture.componentInstance;
     expect(component.res$).toBe(response);
  }));

  //测试routerlink
  it('go to detail page of a recipe',() => {
  response = [{
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
      }];
    component.res$ = response;
    fixture.detectChanges();
    console.log(component.res$);
    el = fixture.debugElement.queryAll(By.css('a'));
    let index: number = 0;
    for(let obj of el){
      let href = obj.nativeElement.getAttribute('href');
      expect(href).toEqual('/recipedetail/' + component.res$[index].id);
      index++;
    };
    el = fixture.debugElement.queryAll(By.css('img'));
    index = 0;
    for(let obj of el){
      expect(obj.nativeElement.src).toEqual(component.res$[index].image_url);
      index++;
    };
    el = fixture.debugElement.queryAll(By.css('h5'));
    index = 0;
    for(let obj of el){
      expect(obj.nativeElement.textContent.trim()).toEqual('#'+(index+1)+ ' ' +component.res$[index].name);
      index++;
    };
    el = fixture.debugElement.queryAll(By.css('p'));
    index = 0;
    for(let obj of el){
      expect(obj.nativeElement.textContent.trim()).toEqual(component.res$[index].description+'...');
      index++;
    };
  })
});
