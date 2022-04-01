import { ComponentFixture, TestBed } from '@angular/core/testing';
import { UserDetailComponent } from './user-detail.component';
import { RecipeService } from '../../../services/recipe.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { UserService } from '../../../services/user.service';
import { BehaviorSubject, of } from 'rxjs';
import { User } from '../../../model/user';
import { CartItem } from '../../../model/cart';
import { RouterTestingModule } from '@angular/router/testing';
import { Observable } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { HttpErrorResponse } from '@angular/common/http';

describe('UserDetailComponent', () => {
  let component: UserDetailComponent;
  let fixture: ComponentFixture<UserDetailComponent>;
  let userService: UserService;
  let el: DebugElement;
  let mockUser: User = {
    username: 'username',
    id: '',
    token: 'token',
    email: 'email',
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
  let mockShipping_address: any = {
    address : 'address',
    province : 'address',
    postal_code : 'code',
    phone_number : 'telephone',
  };
  let mockUserHttp: any = {
    username: 'username',
    id: '',
    token: '',
    email: '',
    credit_card: '',
    shipping_address: null,
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
  let mockUserService = {
    getUser: () => {
      return new BehaviorSubject<User | null>({
        username: 'username',
        // attributes
        id: '',
        token: 'token',
        email: 'email',
        credit_card: '',
        shipping_address: '',

        // date
        last_login: new Date(),
        date_joined: new Date(),
        expiry: new Date(),
        // Types
        is_active: true,
        is_staff: false,
        is_superuser: false,

        // Collections
        cart_items: [],
        orders: [],
        fav_recipes: [],
        groups: [],
        user_permissions: []
      })
    },
    UpdateUser: (
      userInfo: any,
      cardID: string,
      telephone: string,
      address: string,
      province: string,
      postal_code: string,
      userToken: any
    ) => {
      userInfo.credit_card = cardID;
      mockShipping_address = {
        address : address,
        province : province,
        postal_code : postal_code,
        phone_number : telephone,
      };
      userInfo.shipping_address =  mockShipping_address;
      return of(userInfo as any);
    },
    setUserToken: (token: string) => {
      mockUserHttp.token = token;
    },
    getUserToken: () => {
      return mockUserHttp.token;
    },
    setUser: (user: any) => {
      mockUserHttp = user;
    },
  };

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [UserDetailComponent],
      providers: [{ provide: UserService, useValue: mockUserService }],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UserDetailComponent);
    component = fixture.componentInstance;
    userService = TestBed.get(UserService);
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  //首先要获得User
  it('should get user information firstly', () => {
    userService.getUser().subscribe((res: any) => {
      mockUserHttp = res;
    })
    expect(mockUserHttp).not.toBeNull();
    console.log(mockUserHttp);
    expect((mockUserHttp as any).username).toBe(mockUser.username);
    expect((mockUserHttp as any).token).toBe(mockUser.token);
    expect((mockUserHttp as any).email).toBe(mockUser.email);
  });

  //得到user显示出来
  it('should show user information to view after login', () => {
    let mockShipping_address: any = {
      address : 'address',
      province : 'address',
      postal_code : 'code',
      phone_number : 'telephone',
    };
    let mockUserHttp: any = {
      username: 'username',
      id: '',
      token: '',
      email: '',
      credit_card: '',
      shipping_address: null,
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
    mockUserHttp.shipping_address = mockShipping_address;
    mockUserHttp.credit_card = '1234';
    component.userInfo = mockUserHttp;
    el = fixture.debugElement.query(By.css('p.name'));
    expect(el.nativeElement.textContent).toBe(component.userInfo.username);
    el = fixture.debugElement.query(By.css('span#cardEmpty'));
    expect(el.nativeElement.textContent).toBe(component.emptyString);
    el = fixture.debugElement.query(By.css('span#shippingAddress'));
    expect(el.nativeElement.textContent).toBe(component.emptyString);
    el = fixture.debugElement.query(By.css('span#telephone'));
    expect(el.nativeElement.textContent).toBe(component.emptyString);
    component.JudgeIfNull();
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('span.cardId'));
    expect(el.nativeElement.textContent).toBe(component.userInfo.credit_card);
    el = fixture.debugElement.query(By.css('span.shippingAddress'));
    expect(el.nativeElement.textContent).toBe(component.userInfo.shipping_address.address+', '+component.userInfo.shipping_address.province+', '+component.userInfo.shipping_address.postal_code);
    el = fixture.debugElement.query(By.css('span.telephone'));
    expect(el.nativeElement.textContent).toBe(component.userInfo.shipping_address.phone_number);
  });

  //考虑要不要传递usertoken
  it('should send token to service after get user information', () => {
    userService.setUserToken('token');
    expect(mockUserHttp.token).toBe('token');
  });

  //测试一下JudgeNull（简单）
  it('should judge if information of user is null', () => {
    let mockShipping_address: any = {
      address : 'address',
      province : 'address',
      postal_code : 'code',
      phone_number : 'telephone',
    };
    let mockUserHttp: any = {
      username: 'username',
      id: '',
      token: 'token',
      email: '',
      credit_card: '',
      shipping_address: null,
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
    component.userInfo = mockUserHttp;
    component.JudgeIfNull();
    expect(component.ifcardNull).toBe(true);
    expect(component.ifaddressNull).toBe(true);
    expect(component.iftelephoneNull).toBe(true);
    mockUserHttp.credit_card = '1234';
    component.userInfo = mockUserHttp;
    component.JudgeIfNull();
    expect(component.ifcardNull).toBe(false);
    expect(component.ifaddressNull).toBe(true);
    expect(component.iftelephoneNull).toBe(true);
    mockShipping_address = {
      address : '',
      province : '',
      postal_code : '',
      phone_number : '',
    };
    mockUserHttp.shipping_address = mockShipping_address;
    component.userInfo = mockUserHttp;
    component.JudgeIfNull();
    expect(component.ifaddressNull).toBe(true);
    expect(component.iftelephoneNull).toBe(true);
    mockShipping_address = {
      address : 'address',
      province : 'address',
      postal_code : 'code',
      phone_number : 'telephone',
    };
    mockUserHttp.shipping_address = mockShipping_address;
    component.userInfo = mockUserHttp;
    component.JudgeIfNull();
    expect(component.ifaddressNull).toBe(false);
    expect(component.iftelephoneNull).toBe(false);
  });

  //测试一下Change()
  it('should provide form for user to complete information', () => {
    expect(component.isChanging).toBe(false);
    let el: DebugElement;
    el = fixture.debugElement.query(By.css('button.change'));
    el.nativeElement.click();
    expect(component.isChanging).toBe(true);
  });

//   it('input',() => {
//     component.userInfo = mockUserHttp;
//     component.isChanging = true;
//     fixture.detectChanges();
//     el = fixture.debugElement.query(By.css('input#floatingcardID'));
//     el.nativeElement.value = "1234";
//     fixture.detectChanges();
//     console.log('el ',component.cardID);
//     expect(component.cardID).toBe("1234");
//   })

  //Submit，UpdateSucc和updateFail
  it('should update user information successfully when user completes the form', () => {
    userService.UpdateUser(mockUserHttp,'card12341234','phone1234','address','province','postal','userToken').subscribe((res: any) => {
      console.log(res);
    });
//     console.log(mockUserHttp);
//     console.log(mockUserHttp.credit_card);
    expect(mockUserHttp.credit_card).toBe('card12341234');
    expect(mockUserHttp.shipping_address.phone_number).toBe('phone1234');
    expect(mockUserHttp.shipping_address.address).toBe('address');
    expect(mockUserHttp.shipping_address.province).toBe('province');
    expect(mockUserHttp.shipping_address.postal_code).toBe('postal');
    component.onUpdateUserSuccess(mockUserHttp);
    expect(component.isUpdateSucc).toBe(true);
    expect(component.isChanging).toBe(false);
  });

  it('should return error message when user fails to update information', () => {
    const errorInitEvent: ErrorEventInit = {
      error : new Error('Login failed!'),
      message : 'Login failed!',
      lineno : 0,
      colno: 0,
      filename : ''
    };
    const CustomErrorEvent = new ErrorEvent('FailErrorEvent', errorInitEvent);
    component.onUpdateUserError(CustomErrorEvent);
    expect(component.isUpdateSucc).toBe(false);
    component.err_msg = CustomErrorEvent.error;
    expect(component.err_msg).toEqual(CustomErrorEvent.error);
  });

  it('can go to shapping cart page and order page', () => {
    fixture.detectChanges();
    let href = fixture.debugElement.query(By.css('a.shoppingCart')).nativeElement.getAttribute('href');
    expect(href).toEqual('/shoppingcartDetail');
    href = fixture.debugElement.query(By.css('a.orderList')).nativeElement.getAttribute('href');
    expect(href).toEqual('/ordersDetail');
  });

  it('should fail to submit changes when required information is incomplete', () => {
    component.cardID = '';
    component.Submit();
    expect(component.isUpdateSucc).toBe(false);
    expect(component.err_msg).toBe('(information is incomplete)');
    expect(component.isChanging).toBe(true);
    component.address = '';
    component.Submit();
    expect(component.isUpdateSucc).toBe(false);
    expect(component.err_msg).toBe('(information is incomplete)');
    expect(component.isChanging).toBe(true);
    component.telephone = '';
    component.Submit();
    expect(component.isUpdateSucc).toBe(false);
    expect(component.err_msg).toBe('(information is incomplete)');
    expect(component.isChanging).toBe(true);
    component.province = '';
    component.Submit();
    expect(component.isUpdateSucc).toBe(false);
    expect(component.err_msg).toBe('(information is incomplete)');
    expect(component.isChanging).toBe(true);
    component.postal_code = '';
    component.Submit();
    expect(component.isUpdateSucc).toBe(false);
    expect(component.err_msg).toBe('(information is incomplete)');
    expect(component.isChanging).toBe(true);
  });

  it('should submit changes of user information through submit button', () => {
    component.userInfo = mockUserHttp;
    component.cardID = 'card12341234';
    component.telephone = 'phone1234';
    component.address = 'address';
    component.province = 'province';
    component.postal_code = 'postal';
    spyOn(userService,'getUserToken').and.returnValue('token');
    spyOn(userService,'UpdateUser').and.callThrough();
    component.Submit();
    expect(userService.getUserToken).toHaveBeenCalled();
    expect(userService.UpdateUser).toHaveBeenCalled();
  })
});
