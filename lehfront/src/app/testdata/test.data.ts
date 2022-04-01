import { User } from '../model/user';

export const EMPTY_USER: User = {
  username: 'username',
  id: '',
  token: '',
  email: '',
  credit_card: '',
  shipping_address: '',
  last_login: new Date(),
  date_joined: new Date(),
  expiry: new Date(),
  is_active: true,
  is_staff: false,
  is_superuser: false,
  cart_items: [],
  orders: [],
  fav_recipes: [],
  groups: [],
  user_permissions: []
};

export const SAMPLE_USER  =  {
  expiry: new Date("2022-03-28T17:59:57.566575Z"),
  token: "2fa1a29afde6e251d7cbb6fc328106e4ef309938dccb7522bf5ec8683bbdb1de",
  id: "a534b0e6-a681-4d24-a403-dd9876dbc862",
  cart_items: [],
  orders:[],
  shipping_address: "sd",
  last_login: new Date("2022-03-28T07:59:57.568441Z"),
  is_superuser: false,
  is_staff: false,
  is_active: true,
  date_joined: new Date("2022-03-07T15:58:51.345334Z"),
  username: "eugene",
  email: "eugene.r.w.12@gmail.com",
  credit_card: "2222333311117777",
  groups: [],
  user_permissions: [],
  fav_recipes: []
};
