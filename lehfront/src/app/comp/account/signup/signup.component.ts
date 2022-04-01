import { Component, OnInit } from '@angular/core';
import { UserService } from '../../../services/user.service';
import { Router } from '@angular/router';
import { User } from '../../../model/user';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  name = '';
  email = '';
  password = '';
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';

  constructor(private userService: UserService) {}

  ngOnInit(): void {}

  onSignUpSuccess(data: User) {
    //提示注册成功，并且跳转至login页面
    this.isSuccessful = true;
    this.isSignUpFailed = false;
    //         this.router.navigate(['../login']);
  }

  onSignUpError(err: ErrorEvent) {
    this.isSignUpFailed = true;
    this.isSuccessful = false;
    this.errorMessage = err.message;
    console.log(this.errorMessage);
  }

  signUp(): void {
    this.userService.signup(this.name, this.email, this.password).subscribe({
      next: this.onSignUpSuccess.bind(this),
      error: this.onSignUpError.bind(this)
    });
  }
}
