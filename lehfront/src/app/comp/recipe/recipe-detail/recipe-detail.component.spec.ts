import { ComponentFixture, TestBed, fakeAsync, tick } from '@angular/core/testing';
import { RecipeDetailComponent } from './recipe-detail.component';
import { RecipeService } from '../../../services/recipe.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CartService } from '../../../services/cart.service';
import { ActivatedRoute } from '@angular/router';
import { RouterTestingModule } from '@angular/router/testing';
import { Observable, of } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { Recipe } from '../../../model/recipe';
import { CartItem } from '../../../model/cart';
import { Product } from '../../../model/product';
import { UserService } from '../../../services/user.service';

describe('RecipeDetailComponent', () => {
  let component: RecipeDetailComponent;
  let fixture: ComponentFixture<RecipeDetailComponent>;
  let recipeService: RecipeService;
  let cartService: CartService;
  let userService: UserService;
  let response: Recipe[];
  let cart: CartItem[];
  let el: DebugElement;
  let productItem: Product;
  let details: any;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [RecipeDetailComponent],
      providers: [RecipeService, CartService, UserService],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RecipeDetailComponent);
    component = fixture.componentInstance;
    recipeService = TestBed.get(RecipeService);
    cartService = TestBed.get(CartService);
    userService = TestBed.get(UserService);
    details = {
        quantity: [{
          food1: 1,
          food2: 2,
        }],
        instruction: [{
          ins1: 'instruction1',
          ins2: 'instruction2',
        }],
        nutrients: [{
          nutri1: 'nutrient1',
          nutri2: 'nutrient2',
        }],
      };
    response = [{
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
      details: details,
    }];
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should get information of a product item',fakeAsync(() => {
    spyOn(recipeService, 'getRecipe').and.returnValue(of<any[]>(response));
    component.ngOnInit();
    tick();
    expect(component.recipeItem).toBe(response[0]);
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('img'));
    expect(el.nativeElement.src).toEqual(component.recipeItem.image_url);
    el = fixture.debugElement.query(By.css('strong.name'));
    expect(el.nativeElement.textContent.trim()).toBe(component.recipeItem.name);
    el = fixture.debugElement.query(By.css('div.des'));
    expect(el.nativeElement.textContent.trim()).toBe(component.recipeItem.description);
  }));

  it('should disable button for adding to cart without login',() => {
    spyOn(recipeService, 'getRecipe').and.returnValue(of<any[]>(response));
    spyOn(userService, 'getIfLogin').and.returnValue(false);
    component.ngOnInit();
    expect(component.ifLogin).toBe(false);
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('#buttonNot'));
    expect(el.nativeElement.getAttribute('disabled')).toBe('!ifLogin');
  });

  it('should add products through button after login',() => {
    spyOn(recipeService, 'getRecipe').and.returnValue(of<any[]>(response));
    spyOn(userService, 'getIfLogin').and.returnValue(true);
    component.ngOnInit();
    expect(component.ifLogin).toBe(true);
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('#buttonAdd'));
    expect(el).toBeTruthy();
    spyOn(cartService,'addProductsToCart').and.returnValue(of<any[]>(cart));
    el.nativeElement.click();
    expect(cartService.addProductsToCart).toHaveBeenCalled();
  });

  it('can add all ingredients to cart and judge if it succeeds',fakeAsync(() => {
    let productItem = {
      id: 0,
      name: 'test-product',
      description: 'desc',
      price: 99,
      image_url:
        'https://cdn.britannica.com/68/143268-050-917048EA/Beef-loin.jpg',
      category: 'French'
    }
    let cart = [{
      id: 0,
      productId: productItem.id,
      qty: 1,
      product: productItem,
    },
    {
      id: 0,
      productId: response[0].id,
      qty: 1,
      product: response[0],
    }];
    component.recipeItem = response[0];
    spyOn(cartService,'addProductsToCart').and.returnValue(of<any[]>(cart));
    component.handleAddAllToCart();
    tick();
    expect(cartService.addProductsToCart).toHaveBeenCalled();
    component.cartAns = cart as any;
    expect(component.judgeCartAns()).toBeTruthy();
    component.cartAns = [];
    expect(component.judgeCartAns()).toBeFalsy();
  }))

});
