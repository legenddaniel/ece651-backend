import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ShopComponent } from './shop.component';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { RouterTestingModule } from '@angular/router/testing';

describe('ShopComponent', () => {
  let component: ShopComponent;
  let fixture: ComponentFixture<ShopComponent>;
  let el: DebugElement;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ShopComponent],
      imports: [RouterTestingModule],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ShopComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show hot items', () => {
    el = fixture.debugElement.query(By.css('h3#HotItems'));
    expect(el.nativeElement.textContent.trim()).toBe('Hot Items!');
    el = fixture.debugElement.query(By.css('app-carousel'));
    expect(el).toBeTruthy();
  });

  it('should show recipe section', () => {
    el = fixture.debugElement.query(By.css('h3#Recipe'));
    expect(el.nativeElement.textContent.trim()).toBe('Recipe');
    el = fixture.debugElement.query(By.css('app-recipe-section'));
    expect(el).toBeTruthy();
    el = fixture.debugElement.query(By.css('#viewMore'));
    expect(el.nativeElement.textContent.trim()).toBe('View more');
    console.log(el.nativeElement);
    console.log(el);
    expect(el.nativeElement.getAttribute('routerlink')).toEqual('/recipelist');
  });

  it('should show product list', () => {
    el = fixture.debugElement.query(By.css('h3#Produce'));
    expect(el.nativeElement.textContent.trim()).toBe('Products and Ingredients');
    el = fixture.debugElement.query(By.css('app-product-list'));
    expect(el).toBeTruthy();
  });
});
