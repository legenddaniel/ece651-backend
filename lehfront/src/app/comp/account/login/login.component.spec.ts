import { ComponentFixture, TestBed } from '@angular/core/testing';
import { LoginComponent } from './login.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { UserService } from '../../../services/user.service';
import { RouterTestingModule } from '@angular/router/testing';
import { User } from '../../../model/user';
import { Observable, of } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';
import { HttpErrorResponse } from '@angular/common/http';
import { EMPTY_USER, SAMPLE_USER } from '../../../testdata/test.data';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;
  let userService: UserService;
  let mockUser = SAMPLE_USER;
  let el: DebugElement;
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LoginComponent],
      providers: [UserService],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    userService = TestBed.get(UserService);
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should signin an account successfully', () =>{
    spyOn(userService,'login').and.returnValue(of<User>(mockUser));
    component.onSigninSuccess(mockUser);
    expect(component.isSuccessful).toBe(true);
    expect(component.isLoginFailed).toBe(false);
    let user: any;
    userService.getUser().subscribe((res: any) => {
      user = res;
    });
    expect(user).toBe(mockUser);
    expect(userService.getIfLogin()).toBe(true);
  })

  it('should return an error when login failed',() => {
    const errorInitEvent: ErrorEventInit = {
      error : new Error('Login failed!'),
      message : 'Login failed!',
      lineno : 0,
      colno: 0,
      filename : ''
    };
    const CustomErrorEvent = new ErrorEvent('FailErrorEvent', errorInitEvent);
    component.onSignInError(CustomErrorEvent);
//     console.log(CustomErrorEvent.error);
    component.err_msg = CustomErrorEvent.error;
    expect(component.err_msg).toEqual(CustomErrorEvent.error);
    expect(component.isSuccessful).toBe(false);
    expect(component.isLoginFailed).toBe(true);
    expect(userService.getIfLogin()).toBe(false);
  });



  it('should remind user when login failed',() => {
    component.isLoginFailed = true;
    component.err_msg = '';
    fixture.detectChanges();
    el = fixture.debugElement.query(By.css('div.fail'));
    console.log(el.nativeElement);
    expect(el.nativeElement.textContent).toEqual('Login failed,please try again! ');
  });

  it('should show title',() => {
    el = fixture.debugElement.query(By.css('.title'));
    expect(el.nativeElement.textContent).toBe('Log In');
  })

//   it('input', () => {
//     el = fixture.debugElement.query(By.css('#email'));
//     el.nativeElement.value = mockUser.email;
//     fixture.detectChanges();
//     expect(component.email).toBe("test@gmail.com");
//   })
  it('should login through signIn function',() => {
     component.email = 'email@gmail.com';
     component.email = '1234';
     spyOn(userService,'login').and.callThrough();
     component.signIn();
     expect(userService.login).toHaveBeenCalled();
  })
});
