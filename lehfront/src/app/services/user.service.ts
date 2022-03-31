import { Injectable } from '@angular/core';
import { User } from '../model/user';
import { authUrl, userUrl } from 'src/app/config/api';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {
  catchError,
  map,
  Observable,
  throwError,
  tap,
  of,
  Subject,
  Observer,
  BehaviorSubject
} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  ifLogin = false;
  userSubject = new BehaviorSubject<User | null>(null);
  local_user: User | null = null;
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  error_msg = '';
  userToken: any;

  constructor(private http: HttpClient) {}

  setIfLogin(v: boolean) {
    this.ifLogin = v;
  }

  getIfLogin() {
    return this.ifLogin;
  }

  setUserToken(v: any) {
    this.userToken = v;
  }

  getUserToken() {
    return this.userToken;
  }

  setUser(user: User) {
    this.local_user = user;
    this.userSubject.next(user);
  }

  getUser() {
    return this.userSubject;
  }

  signup(name: string, mail: string, pin: string): Observable<User> {
    console.log(name, mail, pin);
    return this.http.post<User>(
      authUrl + 'signup/',
      {
        username: name,
        email: mail,
        password: pin
      },
      this.httpOptions
    );
  }

  login(email: string, password: string): Observable<User> {
    return this.http.post<User>(
      authUrl + 'signin/',
      {
        username: email,
        password: password
      },
      this.httpOptions
    );
  }

  UpdateUser(
    userInfo: any,
    cardID: string,
    telephone: string,
    address: string,
    province: string,
    postal_code: string,
    userToken: any
  ) {
    let httpOptions = {
      headers: new HttpHeaders({
        Authorization: 'Token ' + userToken,
        'Content-Type': 'application/json'
      })
    };
    return this.http.patch(
      userUrl,
      {
        username: userInfo.username,
        credit_card: cardID,
        shipping_address: {
          full_name: userInfo.username,
          phone_number: telephone,
          email: userInfo.email,
          address: address,
          province: province,
          postal_code: postal_code
        }
      },
      httpOptions
    );
  }
}
