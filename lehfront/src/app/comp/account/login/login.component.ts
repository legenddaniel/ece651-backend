import { Component, OnInit } from '@angular/core';
import { User } from '../../../model/user';
import { UserService } from '../../../services/user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email = '';
  password = '';
  err_msg = '';
  isSuccessful = false;
  isLoginFailed = false;

  constructor(private userService: UserService, private router: Router) {}

  onSigninSuccess(data: User) {
    this.isSuccessful = true;
    this.isLoginFailed = false;
    this.userService.setUser(data);
    this.userService.setIfLogin(this.isSuccessful);
    this.router.navigate(['']).catch(console.error);
  }

  onSignInError(err: ErrorEvent) {
    this.err_msg = JSON.stringify(err.error);
    console.log(err);
    this.isSuccessful = false;
    this.isLoginFailed = true;
    this.userService.setIfLogin(this.isSuccessful);
  }

  signIn() {
    this.userService.login(this.email, this.password).subscribe({
      next: this.onSigninSuccess.bind(this),
      error: this.onSignInError.bind(this)
    });
  }
}
