import {
  ComponentFixture,
  TestBed,
  fakeAsync,
  tick,
  async,
  inject
} from '@angular/core/testing';
import { ProductComponent } from './product.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CartService } from '../../../services/cart.service';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { formatCurrency } from '@angular/common';
import { RouterTestingModule } from '@angular/router/testing';

describe('ProductComponent', () => {
  let component: ProductComponent;
  let fixture: ComponentFixture<ProductComponent>;
  let el: DebugElement;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ProductComponent],
      providers: [CartService],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProductComponent);
    component = fixture.componentInstance;
    component.productItem = {
      id: 0,
      name: 'test-product',
      description: 'desc',
      price: 99,
      image_url:
        'https://cdn.britannica.com/68/143268-050-917048EA/Beef-loin.jpg',
      category: 'French'
    };
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('initial one item', () => {
    el = fixture.debugElement.query(By.css('.nameLess'));
    expect(el.nativeElement.textContent.trim()).toBe(
      component.productItem.name
    );
    component.productItem.name = 'Green Bell Pepper';
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('.nameGreater'));
    expect(el.nativeElement.textContent.trim()).toBe(
      component.productItem.name.substr(0,16)+'...'
    );
    el = fixture.debugElement.query(By.css('strong.price'));
    expect(el.nativeElement.textContent.trim()).toEqual(
      formatCurrency(component.productItem.price, 'en_US', '$')
    );
    el = fixture.debugElement.query(By.css('span.lessEqual'));
    expect(el.nativeElement.textContent.trim()).toEqual(
      component.productItem.description
    );
    component.productItem.description = 'lank steak comes from the cow\'s lower chest or abdominal muscle, and is an inexpensive, flavorful, and versatile cut of beef.';
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('span.greater'));
    expect(el.nativeElement.textContent.trim()).toEqual(
      component.productItem.description.substr(0,90) + '...'
    );
    el = fixture.debugElement.query(By.css('img'));
    expect(el.nativeElement.src).toEqual(component.productItem.image_url);
  });

  it('should go to detail page of product', async(() => {
    fixture.detectChanges();
    let href = fixture.debugElement
      .query(By.css('a'))
      .nativeElement.getAttribute('href');
    expect(href).toEqual('/productdetail/' + component.productItem.id);
  }));
});
