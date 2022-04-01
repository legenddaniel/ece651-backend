import { TestBed, fakeAsync, tick } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { AuthGuardService } from './auth-guard.service';
import { UserService } from './user.service';
import { Router } from '@angular/router';

describe('AuthGuardService', () => {
  let service: AuthGuardService;
  let userService: UserService;
  let router = {
    navigate: jasmine.createSpy('navigate')
  };

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [UserService, { provide: Router, useValue: router }]
    });
    service = TestBed.inject(AuthGuardService);
    userService = TestBed.get(UserService);
  });

  it('should return false when ifLogin in userService is false', () => {
    spyOn(userService, 'getIfLogin').and.returnValue(false);
    expect(service.canActivate()).toBe(false);
    expect(router.navigate).toHaveBeenCalledWith(['login']);
  });

  it('should return true when ifLogin in userService is true', () => {
    spyOn(userService, 'getIfLogin').and.returnValue(true);
    expect(service.canActivate()).toBe(true);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
