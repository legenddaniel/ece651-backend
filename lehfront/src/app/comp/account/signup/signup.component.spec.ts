import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SignupComponent } from './signup.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { UserService } from '../../../services/user.service';
import { ActivatedRoute } from '@angular/router';
import { RouterTestingModule } from '@angular/router/testing';
import { User } from '../../../model/user';
import { Observable, of } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { EMPTY_USER } from '../../../testdata/test.data';

describe('SignupComponent', () => {
  let component: SignupComponent;
  let fixture: ComponentFixture<SignupComponent>;
  let userService: UserService;
  let mockUser: User;
  let el: DebugElement;
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SignupComponent],
      providers: [UserService],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SignupComponent);
    component = fixture.componentInstance;
    userService = TestBed.get(UserService);
    mockUser = {
      username: 'username',
      id: '',
      token: '',
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
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should sign up an account successfully', () =>{
    spyOn(userService,'signup').and.returnValue(of<User>(mockUser));
    component.onSignUpSuccess(mockUser);
    expect(component.isSuccessful).toBe(true);
    expect(component.isSignUpFailed).toBe(false);
  });

  it('should return an error when signup failed',() => {
    const errorInitEvent: ErrorEventInit = {
      error : new Error('Login failed!'),
      message : 'Login failed!',
      lineno : 0,
      colno: 0,
      filename : ''
    };
    const CustomErrorEvent = new ErrorEvent('FailErrorEvent', errorInitEvent);
    component.onSignUpError(CustomErrorEvent);
    expect(component.isSuccessful).toBe(false);
    expect(component.isSignUpFailed).toBe(true);
  });

  it('should remind user when signup failed',() => {
    component.isSignUpFailed = true;
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('div.fail'));
    expect(el.nativeElement.textContent).toEqual('Signup failed,please try again!');
  });

  it('should remind user when signup succeeded',() => {
    component.isSuccessful = true;
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('div.succ'));
    expect(el.nativeElement.textContent).toEqual('Your registration is successful!Go to login page now!');
  });

  it('should help user to jump to login page when signup succeeded',() => {
    component.isSuccessful = true;
    fixture.detectChanges();
    let href = fixture.debugElement.query(By.css('a.login')).nativeElement.getAttribute('href');
    expect(href).toEqual('/login');
  });

  it('should show title',() => {
    el = fixture.debugElement.query(By.css('.title'));
    expect(el.nativeElement.textContent).toBe('Create an account');
  });

    it('should login through signIn function',() => {
     component.email = 'email@gmail.com';
     component.name = 'name';
     component.email = '1234';
     spyOn(userService,'signup').and.callThrough();
     component.signUp();
     expect(userService.signup).toHaveBeenCalled();
  })

  it('should be able to call SigIn()', () => {
    let spy = spyOn(userService, 'signup').and.returnValue(of(EMPTY_USER));
    component.signUp();
    expect(spy).toHaveBeenCalled();
  })
});
