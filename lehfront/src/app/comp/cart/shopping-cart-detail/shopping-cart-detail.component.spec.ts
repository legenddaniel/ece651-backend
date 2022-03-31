import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShoppingCartDetailComponent } from './shopping-cart-detail.component';
import { RecipeService } from '../../../services/recipe.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CartService } from '../../../services/cart.service';

describe('ShoppingCartDetailComponent', () => {
  let component: ShoppingCartDetailComponent;
  let fixture: ComponentFixture<ShoppingCartDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ShoppingCartDetailComponent],
      providers: [CartService],
      imports: [HttpClientTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ShoppingCartDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
