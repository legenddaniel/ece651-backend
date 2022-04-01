import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FooterComponent } from './comp/common/footer/footer.component';
import { NavComponent } from './comp/common/nav/nav.component';
import { PageNotFoundComponent } from './comp/common/notfound/page-not-found.component';
import { ShopComponent } from './comp/shop/shop.component';
import { ProductListComponent } from './comp/product/product-list/product-list.component';
import { ProductComponent } from './comp/product/product-item/product.component';
import { HttpClientModule } from '@angular/common/http';
import { CartComponent } from './comp/cart/cart-list/cart.component';
import { CartItemComponent } from './comp/cart/cart-item/cart-item.component';
import { RecipeItemComponent } from './comp/recipe/recipe-item/recipe-item.component';
import { RecipeListComponent } from './comp/recipe/recipe-list/recipe-list.component';
import { UserDetailComponent } from './comp/page/user-detail/user-detail.component';
import { ProductDetailComponent } from './comp/product/product-detail/product-detail.component';
import { RecipeDetailComponent } from './comp/recipe/recipe-detail/recipe-detail.component';
import { RatingComponent } from './comp/common/rating/rating.component';
import { CarouselComponent } from './comp/common/carousel/carousel.component';
import { ShoppingCartDetailComponent } from './comp/cart/shopping-cart-detail/shopping-cart-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CarouselModule } from 'ngx-bootstrap/carousel';
import { NgxNumberSpinnerModule } from 'ngx-number-spinner';
import { RatingModule } from 'ngx-bootstrap/rating';
import { FormsModule } from '@angular/forms';
import { SearchComponent } from './comp/common/search/search.component';
import { TypeaheadModule } from 'ngx-bootstrap/typeahead';
import { LoginComponent } from './comp/account/login/login.component';
import { SignupComponent } from './comp/account/signup/signup.component';
import { RecipeSectionComponent } from './comp/recipe/recipe-section/recipe-section.component';
import { OrderDetailComponent } from './comp/page/order-detail/order-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    NavComponent,
    PageNotFoundComponent,
    ShopComponent,
    ProductListComponent,
    ProductComponent,
    CartComponent,
    CartItemComponent,
    RecipeItemComponent,
    RecipeListComponent,
    UserDetailComponent,
    ProductDetailComponent,
    RecipeDetailComponent,
    ProductDetailComponent,
    RatingComponent,
    CarouselComponent,
    ShoppingCartDetailComponent,
    SearchComponent,
    LoginComponent,
    SignupComponent,
    RecipeSectionComponent,
    OrderDetailComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    NgxNumberSpinnerModule,
    CarouselModule.forRoot(),
    TypeaheadModule.forRoot(),
    RatingModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
