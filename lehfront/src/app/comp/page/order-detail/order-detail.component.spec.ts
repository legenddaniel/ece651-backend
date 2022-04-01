import { ComponentFixture, TestBed, fakeAsync, tick } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { OrderDetailComponent } from './order-detail.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { OrderService } from '../../../services/order.service';
import { ActivatedRoute } from '@angular/router';
import { DebugElement } from '@angular/core';
import { of } from 'rxjs';
import { formatCurrency } from '@angular/common';

describe('OrderDetailComponent', () => {
  let component: OrderDetailComponent;
  let fixture: ComponentFixture<OrderDetailComponent>;
  let orderService: OrderService;
  let el: DebugElement;
  let response: any[];

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [OrderDetailComponent],
      providers: [OrderService],
      imports: [HttpClientTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OrderDetailComponent);
    component = fixture.componentInstance;
    orderService = TestBed.get(OrderService);
    response = [
      {
        id: 10,
        subtotal: 800,
        order_items: [
          {
            product: {
              id: 1, name: 'mock_product1', price: 100, image_url:
                'http://cdn.britannica.com/68/143268-050-917048EA/Beef-loin.jpg',
            },
            quantity: 1
          },
          {
            product: {
              id: 1, name: 'mock_product2', price: 200, image_url:
                'http://i5.walmartimages.ca/images/Enlarge/082/821/999999-628915082821.jpg',
            },
            quantity: 2
          }
        ],
      },
      {
        id: 11,
        subtotal: 900,
        order_items: [
          {
            product: {
              id: 1, name: 'mock_product3', price: 100, image_url:
                'http://i5.walmartimages.ca/images/Large/460/938/6000199460938.jpg',
            },
            quantity: 3
          },
          {
            product: {
              id: 1, name: 'mock_product4', price: 200, image_url:
                'http://i5.walmartimages.ca/images/Large/032/768/6000202032768.jpg',
            },
            quantity: 4
          }
        ],
      }
    ];
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should get order list', fakeAsync(() => {
    spyOn(orderService, 'getAllOrders').and.returnValue(of<any>(response));
    component.ngOnInit();
    expect(component.orders).toBe(response);
  }));

  it('should display breadcrumb navigation and h2', () => {

    el = fixture.debugElement.query(By.css('span.nav-account'));
    expect(el.nativeElement.textContent.trim()).toEqual('Your account >');
    el = fixture.debugElement.query(By.css('span.nav-order'));
    expect(el.nativeElement.textContent.trim()).toEqual('Your orders');
    el = fixture.debugElement.query(By.css('h2'));
    expect(el.nativeElement.textContent.trim()).toEqual('Your orders');
  });

  it('should display order id, order subtotal price', () => {
    let el: DebugElement[];
    component.orders = response.reverse();
    fixture.detectChanges();
    el = fixture.debugElement.queryAll(By.css('div.order-id'));
    // notice most recent order is displayed first
    el = el.reverse()
    for (let i = 0; i < el.length; i++) {
      expect(el[i].nativeElement.textContent.trim()).toBe(
        'order ' + component.orders[i].id
      );
    }

    el = fixture.debugElement.queryAll(By.css('div.total'));
    el = el.reverse()
    for (let i = 0; i < el.length; i++) {
      console.log('order subtotal =', el[i].nativeElement.textContent.trim())
      expect(el[i].nativeElement.textContent.trim()).toBe(
        'Total: ' + formatCurrency(component.orders[i].subtotal, 'en_US', '$')
      );
    }
  });

  it('should display products in the order, each product should display name, image, price, and quantity', () => {
    let el: DebugElement[];
    // new order should be displayed first
    component.orders = response;
    fixture.detectChanges();

    // test name
    el = fixture.debugElement.queryAll(By.css('div.item-name'));
    let mock_name = []

    for (let order of component.orders.reverse()){
      for(let item of order.order_items){
        mock_name.push(item.product.name)
      }     
    }
    for(let i=0; i<mock_name.length; i++){
      expect(el[i].nativeElement.textContent.trim()).toBe(
        mock_name[i]
      );
    }

    // test quantity
    el = fixture.debugElement.queryAll(By.css('div.item-quantity'));
    let mock_quantity = []
    for (let order of component.orders){
      for(let item of order.order_items){
        console.log('product name = ', item.quantity)
        mock_quantity.push('x '+item.quantity)
      }     
    }
    for(let i=0; i<mock_quantity.length; i++){
      expect(el[i].nativeElement.textContent.trim()).toBe(
        mock_quantity[i]
      );
    }

    // test price
    el = fixture.debugElement.queryAll(By.css('div.item-price'));
    for(let i=0; i<el.length; i++){
      console.log('el =',el[i].nativeElement.textContent.trim())
    }
    let mock_price = []
    for (let order of component.orders){
      for(let item of order.order_items){
        let temp = formatCurrency(item.product.price, 'en_US', '$')
        mock_price.push(temp)
      }     
    }
    for(let i=0; i<mock_price.length; i++){
      expect(el[i].nativeElement.textContent.trim()).toBe(
        mock_price[i]
      );
    }

    // test img_url
    el = fixture.debugElement.queryAll(By.css('img'));
    for(let i=0; i<el.length; i++){
      console.log('el =',el[i].nativeElement.src)
    }
    let mock_image = []
    for (let order of component.orders){
      for(let item of order.order_items){
        mock_image.push(item.product.image_url)
      }     
    }
    for(let i=0; i<mock_image.length; i++){
      expect(el[i].nativeElement.src).toBe(
        mock_image[i]
      );
    }

  });
});
