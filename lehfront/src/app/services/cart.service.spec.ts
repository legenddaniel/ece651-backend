import { fakeAsync, TestBed, tick } from '@angular/core/testing';

import { CartService } from './cart.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { cartUrl, productsUrl } from '../config/api';
import { UserService } from './user.service';
import { BehaviorSubject } from 'rxjs';
import { User } from '../model/user';
import { SAMPLE_USER } from '../testdata/test.data';

describe('CartService', () => {
  let service: CartService;
  let httpTestingController: HttpTestingController;
  let response = {}
  let product = {
    id: 0,
    name: 'test-product',
    description: 'desc',
    price: 99,
    image_url:
      'https://cdn.britannica.com/68/143268-050-917048EA/Beef-loin.jpg',
    category: 'French'
  };

  let user = {
    expiry: new Date("2022-03-28T17:59:57.566575Z"),
    token: "2fa1a29afde6e251d7cbb6fc328106e4ef309938dccb7522bf5ec8683bbdb1de",
    id: "a534b0e6-a681-4d24-a403-dd9876dbc862",
    cart_items: [],
    orders:[],
    shipping_address: "sd",
    last_login: new Date("2022-03-28T07:59:57.568441Z"),
    is_superuser: false,
    is_staff: false,
    is_active: true,
    date_joined: new Date("2022-03-07T15:58:51.345334Z"),
    username: "eugene",
    email: "eugene.r.w.12@gmail.com",
    credit_card: "2222333311117777",
    groups: [],
    user_permissions: [],
    fav_recipes: []
  }

  let userServiceStub: Partial<UserService>= {
    getUser(): BehaviorSubject<User | null> {
      return new BehaviorSubject<User | null>(SAMPLE_USER);
    }
  }

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CartService, {provide: UserService, useValue:userServiceStub }],
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(CartService);
    service.user = user;

    httpTestingController = TestBed.get(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('Should not get cart without user object', fakeAsync(() => {
    service.user = null;
    service.getCartItems().subscribe((res) => {
      expect(res).toBeTruthy();
      expect(res.length).toBe(0);
    });
    tick();
  }));

  it('Should get cart user object', fakeAsync(() => {
    service.getCartItems().subscribe((res) => {
      expect(res).toBeTruthy();
    });
    tick();
  }));

  it('Should not add product to cart with user object', fakeAsync(() => {
    service.user = null;
    service.addProductToCart(product, 3).subscribe((res) => {
      expect(res).toBeTruthy();
      expect(res.length).toBe(0);
    });
    tick();
  }));

  it('Should add product to cart with user object', fakeAsync(() => {
    service.addProductToCart(product, 3).subscribe((res) => {
      expect(res).toBeTruthy()
    });
    tick();
  }));

  it('Should not add products to cart without user object', fakeAsync(() => {
    service.user = null;
    service.addProductsToCart([{product_id: 2, quantity: 1}]).subscribe((res) => {
      expect(res).toBeTruthy();
      expect(res.length).toBe(0);
    });
    tick();
  }));

  it('Should add products to kart', fakeAsync(() => {
    service.addProductsToCart([{product_id: 2, quantity: 1}]).subscribe((res) => {
      expect(res).toBeTruthy()
    });
    tick();
  }));

  it('Should not get delete product from cart without user', fakeAsync(() => {
    service.user = null
    service.delProduct(0).subscribe((res) => {
      expect(res).toBeTruthy()
      expect((res as any[]).length).toEqual(0);
    });
    tick();
  }));

  it('Should get delete product from cart', fakeAsync(() => {
    service.delProduct(0).subscribe((res) => {
      expect(res).toBeTruthy()
    });
    tick();
  }));

  it('Should not create new order without user', fakeAsync(() => {
    service.user = null;
    service.create_new_order('unpaid', [{product_id: 1, quantity: 1}]).subscribe((res) => {
      expect(res).toBeTruthy();
      expect((res as any[]).length).toEqual(0);
    });
    tick();
  }));

  it('Should create new order ', fakeAsync(() => {
    service.create_new_order('unpaid', [{product_id: 1, quantity: 1}]).subscribe((res) => {
      expect(res).toBeTruthy()
    });
    tick();
  }));
});
