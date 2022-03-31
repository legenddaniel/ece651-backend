import { TestBed, fakeAsync, tick } from '@angular/core/testing';
import { User } from '../model/user';
import { UserService } from './user.service';
import {
  HttpClientTestingModule,
  HttpTestingController
} from '@angular/common/http/testing';
import { BehaviorSubject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { authUrl, userUrl } from 'src/app/config/api';
import { EMPTY_USER } from '../testdata/test.data';

describe('UserService', () => {
  let service: UserService;
  let httpTestingController: HttpTestingController;
  let user = EMPTY_USER;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(UserService);
    httpTestingController = TestBed.get(HttpTestingController);
  });

  afterEach(() => {
    // After every test, assert that there are no more pending requests.
    httpTestingController.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('set value to ifLogin', () => {
    service.setIfLogin(false);
    expect(service.ifLogin).toBe(false);
    service.setIfLogin(true);
    expect(service.ifLogin).toBe(true);
  });

  it('get value of ifLogin', () => {
    service.ifLogin = false;
    expect(service.getIfLogin()).toBe(false);
    service.ifLogin = true;
    expect(service.getIfLogin()).toBe(true);
  });

  it('set value to userToken', () => {
    service.setUserToken('token');
    expect(service.userToken).toBe('token');
  });

  it('get value of userToken', () => {
    service.userToken = 'token';
    expect(service.getUserToken()).toBe('token');
  });

  it('set value to user', () => {
    service.setUser(user);
    expect(service.local_user).toBe(user);
  });

  it('get value of user', () => {
    let mockUser: BehaviorSubject<User | null> =
      new BehaviorSubject<User | null>(user);
    service.userSubject = mockUser;
    expect(service.getUser()).toBe(mockUser);
  });

  it('signup and create account', fakeAsync(() => {
    let response = {
      username: 'username',
      email: 'email@uwaterloo.ca',
      password: 'pin'
    };
    service.signup('username', 'email@uwaterloo.ca', 'pin').subscribe((res) => {
      expect(res.username).toEqual(response.username);
      expect(res.email).toEqual(response.email);
    });
    const req = httpTestingController.expectOne(authUrl + 'signup/');
    // Assert that the request is a GET.
    expect(req.request.method).toEqual('POST');
    // Respond with this data when called
    req.flush(response);
    // Call tick whic actually processes te response
    tick();
  }));

  it('signin and login account', fakeAsync(() => {
    let response = {
      username: 'email@uwaterloo.ca',
      password: 'pin'
    };
    service.login('email@uwaterloo.ca', 'pin').subscribe((res) => {
      expect(res.username).toEqual(response.username);
    });
    const req = httpTestingController.expectOne(authUrl + 'signin/');
    expect(req.request.method).toEqual('POST');
    req.flush(response);
    tick();
  }));

  it('update account information', fakeAsync(() => {
    let user: User = {
      username: 'username',
      id: '',
      token: 'token',
      email: 'email@uwaterloo.ca',
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
    };
    let response = {
      username: 'username',
      email: 'email@uwaterloo.ca',
      password: 'pin',
      cardID: '1111222233334444',
      telephone: '1112223333',
      address: 'address',
      province: 'province',
      postal_code: 'N2L0E1'
    };
    service
      .UpdateUser(
        user,
        '1111222233334444',
        '1112223333',
        'address',
        'province',
        'N2L0E1',
        user.token
      )
      .subscribe((res) => {
        console.log(res);
        expect((res as any).cardID).toBe(response.cardID);
        expect((res as any).telephone).toBe(response.telephone);
        expect((res as any).address).toBe(response.address);
        expect((res as any).province).toBe(response.province);
        expect((res as any).postal_code).toBe(response.postal_code);
      });
    const req = httpTestingController.expectOne(userUrl);
    expect(req.request.method).toEqual('PATCH');
    req.flush(response);
    tick();
  }));
});
