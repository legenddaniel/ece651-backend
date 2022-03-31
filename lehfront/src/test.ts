// This file is required by karma.conf.js and loads recursively all the .spec and framework files

import 'zone.js/testing';
import { getTestBed } from '@angular/core/testing';
import {
  BrowserDynamicTestingModule,
  platformBrowserDynamicTesting
} from '@angular/platform-browser-dynamic/testing';

declare const require: {
  context(
    path: string,
    deep?: boolean,
    filter?: RegExp
  ): {
    keys(): string[];
    <T>(id: string): T;
  };
};

// First, initialize the Angular testing environment.
getTestBed().initTestEnvironment(
  BrowserDynamicTestingModule,
  platformBrowserDynamicTesting()
);

// Then we find all the tests.
const context = require.context('./', true, /\.spec\.ts$/);
// And load the modules.
context.keys().map(context);
// const FILE = ['./app/services/user.service.spec.ts'];
// const FILE = ['./app/comp/product/product-detail/product-detail.component.spec.ts'];
// const FILE = ['./app/comp/recipe/recipe-detail/recipe-detail.component.spec.ts'];
// const FILE = ['./app/comp/recipe/recipe-section/recipe-section.component.spec.ts'];
// const FILE = ['./app/comp/common/nav/nav.component.spec.ts'];
// const FILE = ['./app/comp/page/user-detail/user-detail.component.spec.ts'];
// const FILE = ['./app/comp/account/login/login.component.spec.ts'];

// const FILE = ['./app/comp/page/order-detail/order-detail.component.spec.ts'];
// const FILE = ['./app/comp/shop/shop.component.spec.ts'];

// context.keys().filter( name => !!FILE.includes(name)).map(context);
