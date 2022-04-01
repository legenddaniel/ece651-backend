import { Component, OnInit, Input } from '@angular/core';
import { map, Observable, Observer, of, switchMap } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { RecipeService } from '../../../services/recipe.service';
import { Recipe } from '../../../model/recipe';
import { ProductService } from '../../../services/product.service';
import { Router } from '@angular/router';
import { UserService } from '../../../services/user.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
  ifLogin = false;
  username = '';
  recipe: any[] = [];
  product: any[] = [];
  collapsedShow = false;
  collapsedShowState = '';
  search_text = '';

  constructor(
    private recipeService: RecipeService,
    private productService: ProductService,
    private userService: UserService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.recipeService.getRecipes().subscribe((it) => {
      this.recipe.push(...it);
    });

    this.productService.getProducts().subscribe((it) => {
      this.product.push(...it);
    });

    this.userService.getUser().subscribe((user: any) => {
      if(user != null){
        this.username = user.username;
        this.ifLogin = true;
        console.log('user from service');
        console.log(user);
      }
    });
  }

  look() {
    this.router.navigate(['/search', this.search_text]);
  }
}
