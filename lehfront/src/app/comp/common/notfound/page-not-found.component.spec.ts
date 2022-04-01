import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { Router } from '@angular/router';
import { PageNotFoundComponent } from './page-not-found.component';
import { Observable, of } from 'rxjs';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';

describe('PageNotFoundComponent', () => {
  let component: PageNotFoundComponent;
  let fixture: ComponentFixture<PageNotFoundComponent>;
  let el: DebugElement;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [PageNotFoundComponent],
      imports: [HttpClientTestingModule, RouterTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PageNotFoundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  //主要测试routerlink
  it('can go to home page', () =>{
    el = fixture.debugElement.query(By.css('a'));
    expect(el.nativeElement.getAttribute('href')).toBe('/');
  });

  it('should display title', () =>{
    el = fixture.debugElement.query(By.css('h3'));
    expect(el.nativeElement.textContent.trim()).toBe('404 - Page Not Found');
  });

  it('should remind user', () =>{
    el = fixture.debugElement.query(By.css('p'));
    expect(el.nativeElement.textContent.trim()).toBe('Oops! The page that you were looking for is not found.');
  });
});
