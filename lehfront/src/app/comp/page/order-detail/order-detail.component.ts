import { Component, OnInit } from '@angular/core';
import { User } from '../../../model/user';
import { OrderService } from '../../../services/order.service';
@Component({
  selector: 'app-order-detail',
  templateUrl: './order-detail.component.html',
  styleUrls: ['./order-detail.component.css']
})
export class OrderDetailComponent implements OnInit {
  constructor(private oServ: OrderService) { }
  user: User | null = null;
  orders: any[] = [];

  ngOnInit(): void {
    console.log('Order Detail');
    this.oServ.getAllOrders().subscribe((it) => {
      this.orders = it;
      console.log('I am trying to get all orders!');
      console.log(it);
      console.log('url = ', it[0].order_items[0].product.image_url);
    }
    );
  }
}
