import { TestBed, fakeAsync, tick } from '@angular/core/testing';
import { ProductService } from './product.service';
import {
  HttpClientTestingModule,
  HttpTestingController
} from '@angular/common/http/testing';
import { HttpClient } from '@angular/common/http';
import { Product } from '../model/product';
import { productsUrl } from 'src/app/config/api';

describe('ProductService', () => {
  let service: ProductService;
  let httpTestingController: HttpTestingController;
  let response: Product;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(ProductService);
    httpTestingController = TestBed.get(HttpTestingController);
    response = {
      id: 0,
      name: 'test-product',
      description: 'desc',
      price: 99,
      image_url:
        'https://cdn.britannica.com/68/143268-050-917048EA/Beef-loin.jpg',
      category: 'French'
    };
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('get all products', fakeAsync(() => {
    service.getProducts().subscribe((res) => {
      expect((res as any).id).toBe(response.id);
      expect((res as any).name).toBe(response.name);
      expect((res as any).description).toBe(response.description);
      expect((res as any).image_url).toBe(response.image_url);
      expect((res as any).price).toBe(response.price);
    });
    const req = httpTestingController.expectOne(productsUrl);
    expect(req.request.method).toEqual('GET');
    req.flush(response);
    tick();
  }));

  it('get product by id', fakeAsync(() => {
    service.getProduct(response.id).subscribe((res) => {
      expect((res as any).id).toBe(response.id);
    });
    const req = httpTestingController.expectOne(
      productsUrl + '?id=' + response.id
    );
    expect(req.request.method).toEqual('GET');
    req.flush(response);
    tick();
  }));

  it('get product by name', fakeAsync(() => {
    service.getProductByName(response.name).subscribe((res) => {
      expect((res as any).name).toBe(response.name);
    });
    const req = httpTestingController.expectOne(
      productsUrl + '?name=' + response.name
    );
    expect(req.request.method).toEqual('GET');
    req.flush(response);
    tick();
  }));
});
