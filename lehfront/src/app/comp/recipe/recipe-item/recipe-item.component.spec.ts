import {
  ComponentFixture,
  TestBed,
  fakeAsync,
  tick,
  async,
  inject
} from '@angular/core/testing';
import { RecipeItemComponent } from './recipe-item.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CartService } from '../../../services/cart.service';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { RouterTestingModule } from '@angular/router/testing';
import { Router } from '@angular/router';
import { Location } from '@angular/common';
import { SpyLocation } from '@angular/common/testing';

describe('RecipeComponent', () => {
  let component: RecipeItemComponent;
  let fixture: ComponentFixture<RecipeItemComponent>;
  let el: DebugElement;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [RecipeItemComponent],
      providers: [CartService],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RecipeItemComponent);
    component = fixture.componentInstance;
    component.recipeItem = {
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
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('initial one item', () => {
    el = fixture.debugElement.query(By.css('span.nameLess'));
    expect(el.nativeElement.textContent.trim()).toBe(component.recipeItem.name);
    component.recipeItem.name = 'Flank Steak with Tangy Yogurt Sauce';
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('span.nameGreater'));
    expect(el.nativeElement.textContent.trim()).toEqual(
      component.recipeItem.name.substr(0,25) + '...'
    );
    el = fixture.debugElement.query(By.css('span.lessEqual'));
    expect(el.nativeElement.textContent.trim()).toEqual(
      component.recipeItem.description
    );
    component.recipeItem.description = 'Ultimate Slow Cooker Pot Roast that leaves you with tender meat, vegetables and a built in gravy to enjoy them all with in just 15 minutes of prep! Perfect weeknight dinner! No-fuss, amazingly fall-apart pot roast made in your crockpot with the most tender vegetables!';
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('span.greater'));
    expect(el.nativeElement.textContent.trim()).toEqual(
      component.recipeItem.description.substr(0,160) + '...'
    );
    el = fixture.debugElement.query(By.css('img'));
    expect(el.nativeElement.src).toEqual(component.recipeItem.image_url);
  });

  it('should go to detail page of recipe', async(() => {
    fixture.detectChanges();
    let href = fixture.debugElement
      .query(By.css('a'))
      .nativeElement.getAttribute('href');
    expect(href).toEqual('/recipedetail/' + component.recipeItem.id);
  }));
});
