import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, Observable, throwError } from 'rxjs';
import { Product } from '../model/product';
import { productsUrl } from 'src/app/config/api';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  constructor(private http: HttpClient) {}

  getProduct(id: number): Observable<Product[]> {
    return this.http.get<Product[]>(productsUrl + '?id=' + id);
  }

  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(productsUrl);
  }

  getProductByName(name: string): Observable<Product[]> {
    return this.http.get<Product[]>(productsUrl + '?name=' + name);
  }
}
