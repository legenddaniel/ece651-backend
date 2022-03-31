import { ComponentFixture, TestBed, fakeAsync, tick, inject } from '@angular/core/testing';
import { NavComponent } from './nav.component';
import { RecipeService } from '../../../services/recipe.service';
import { ProductService } from '../../../services/product.service';
import { UserService } from '../../../services/user.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { Product } from '../../../model/product';
import { Recipe } from '../../../model/recipe';
import { User } from '../../../model/user';
import { Observable, of } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';

describe('NavComponent', () => {
  let component: NavComponent;
  let fixture: ComponentFixture<NavComponent>;
  let recipeService: RecipeService;
  let productService: ProductService;
  let userService: UserService;
  let recipes: Recipe[] = [];
  let products: Product[] = [];
  let el: DebugElement;
  let router = {
    navigate: jasmine.createSpy('navigate')
  };
  const routerSpy = jasmine.createSpyObj('Router', ['navigateByUrl']);

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [NavComponent],
      providers: [RecipeService, ProductService, UserService],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NavComponent);
    component = fixture.componentInstance;
    recipeService = TestBed.get(RecipeService);
    productService = TestBed.get(ProductService);
    userService = TestBed.get(UserService);
    router = TestBed.get(Router);
    recipes = [{
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
    }];
    products = [{
      id: 0,
      name: 'test-product',
      description: 'desc',
      price: 99,
      image_url:
        'https://cdn.britannica.com/68/143268-050-917048EA/Beef-loin.jpg',
      category: 'French'
    }];
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('can get all recipes for searching', () => {
    spyOn(recipeService, 'getRecipes').and.returnValue(of<any[]>(recipes));
    component.ngOnInit();
    expect(component.recipe).toEqual(recipes);
  });

  it('can get all products for searching', () => {
    spyOn(productService, 'getProducts').and.returnValue(of<any[]>(products));
    component.ngOnInit();
    expect(component.product).toEqual(products);
  });

  it('should show user information', () => {
    expect(component.ifLogin).toBe(false);
    let mockUser: BehaviorSubject<User | null> =
      new BehaviorSubject<User | null>({
        username: 'username',
        id: '',
        token: '',
        email: '',
        credit_card: '',
        shipping_address: '',
        last_login: new Date(),
        date_joined: new Date(),
        expiry: new Date(),
        is_active: true,
        is_staff: false,
        is_superuser: false,
        cart_items: [],
        orders: [],
        fav_recipes: [],
        groups: [],
        user_permissions: []
      });
    spyOn(userService, 'getUser').and.returnValue(mockUser);
    let user: any;
    userService.getUser().subscribe((res: any) => {
      user = res;
    });
    component.ngOnInit();
    expect(component.username).toEqual(user.username);
    fixture.detectChanges();
    let el: DebugElement;
    el = fixture.debugElement.query(By.css('span.username'));
    console.log(el);
    expect(el.nativeElement.textContent.trim()).toBe(user.username);
    expect(component.ifLogin).toBe(true);
  });

  it('should jump to login page by clicking \'login\' ', () => {
    component.ifLogin = false;
    fixture.detectChanges();
    let href = fixture.debugElement.query(By.css('a.login')).nativeElement.getAttribute('href');
    expect(href).toEqual('/login');
  });

  it('should jump to signup page by clicking \'signup\' ', () => {
    component.ifLogin = false;
    fixture.detectChanges();
    let href = fixture.debugElement.query(By.css('a.signup')).nativeElement.getAttribute('href');
    expect(href).toEqual('/signup');
  });

  it('should jump to userdetail page by clicking user image', () => {
    component.ifLogin = true;
    fixture.detectChanges();
    let href = fixture.debugElement.query(By.css('a.userDetail')).nativeElement.getAttribute('href');
    expect(href).toEqual('/userdetail');
  });

  it('should jump to recipe list page by clicking \'recipe\'', () => {
    let href = fixture.debugElement.query(By.css('a.recipelist')).nativeElement.getAttribute('href');
    expect(href).toEqual('/recipelist');
  });

  it('should jump to product list page by clicking \'product\'', () => {
    let href = fixture.debugElement.query(By.css('a.productlist')).nativeElement.getAttribute('href');
    expect(href).toEqual('/productlist');
  });

  it('should look for the relevent text', inject([Router], (router: Router) => {
      component.search_text = 'xd';
      spyOn(router, 'navigate').and.stub();
      component.look();
      expect(router.navigate).toHaveBeenCalledWith(['/search', component.search_text]);
    }));
});
