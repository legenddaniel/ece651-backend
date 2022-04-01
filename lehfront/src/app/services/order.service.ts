import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map, Observable, of } from 'rxjs';
import { orderUrl } from '../config/api';
import { UserService } from './user.service';
import { User } from '../model/user';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  index = 5;
  user: User | null = null;
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(
    private http: HttpClient,
    private userService: UserService
  ) {
    this.userService.getUser().subscribe((user) => {
      this.user = user;
      if (this.user != null) {
        this.httpOptions = {
          headers: new HttpHeaders({
            'Content-Type': 'application/json',
            Authorization: 'Token ' + this.user.token
          })
        };
      }
    });
  }

  getAllOrders(): Observable<any> {
    if (!this.user) return of([]);
    console.log('getAllOrders');
    console.log(this.user);
    console.log(this.httpOptions);
    this.httpOptions.headers.set('Authorization', 'token ' + this.user.token);
    return this.http.get<any>(orderUrl, this.httpOptions);
  }
}
