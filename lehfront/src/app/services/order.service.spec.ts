import { fakeAsync, TestBed, tick } from '@angular/core/testing';

import { OrderService } from './order.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { UserService } from './user.service';
import { BehaviorSubject } from 'rxjs';
import { User } from '../model/user';
import { SAMPLE_USER } from '../testdata/test.data';

describe('OrderService', () => {
  let service: OrderService;
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
      imports: [HttpClientTestingModule],
      providers : [ {provide: UserService, useValue: userServiceStub}]
    });
    service = TestBed.inject(OrderService);
  });


  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('Should not get all orders without user object', fakeAsync(() => {
    service.user = null;
    service.getAllOrders().subscribe((res) => {
      expect(res).toBeTruthy();
      expect(res.length).toBe(0);
    });
    tick();
  }));

  it('should get all Orders', fakeAsync(() => {
    service.user = user;
    service.getAllOrders().subscribe((res) => {
      expect(res).toBeTruthy();
      expect(res.length).toBe(0);
    });
    tick();
  }));

});
