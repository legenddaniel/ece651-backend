import {
  ComponentFixture,
  TestBed,
  fakeAsync,
  tick
} from '@angular/core/testing';
import { ProductListComponent } from './product-list.component';
import { RecipeService } from '../../../services/recipe.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ProductService } from '../../../services/product.service';
import { Product } from '../../../model/product';
import { Observable, of } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { HttpClient, HttpHeaders, HttpHandler } from '@angular/common/http';

describe('ProductListComponent', () => {
  let component: ProductListComponent;
  let fixture: ComponentFixture<ProductListComponent>;
  let productService: ProductService;
  let response: Product[];
  let el: DebugElement[];

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ProductListComponent],
      providers: [ProductService],
      imports: [HttpClientTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProductListComponent);
    component = fixture.componentInstance;
    productService = TestBed.get(ProductService);
    response = [
      {
        id: 0,
        name: 'test-product1',
        description: 'desc1',
        price: 1,
        image_url:
          'https://cdn.britannica.com/68/143268-050-917048EA/Beef-loin.jpg',
        category: 'French'
      },
      {
        id: 1,
        name: 'test-product2',
        description: 'desc2',
        price: 2,
        image_url:
          'https://cdn.britannica.com/68/143268-050-917048EA/Beef-loin.jpg',
        category: 'French'
      }
    ];
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should get product list', fakeAsync(() => {
    spyOn(productService, 'getProducts').and.returnValue(of<any[]>(response));
    component.loadProducts();
    expect(component.productList).toBe(response);
    el = fixture.debugElement.queryAll(By.css('app-product-item'));
    expect(el).toBeTruthy();
  }));
});
