# Tutorial

- Install only Python (≥ 3.9) and Docker on your machine. You may need quite some settings for Docker.
- Open project in code editor. Create `.env` at root dir.
- Open terminal at root dir, run `./leh build` then `./leh start`. The server is running properly if you see:
```
...
db_1   | 2022-01-16 19:21:20.950 UTC [1] LOG:  database system is ready to accept connections
...
app_1  | Quit the server with CONTROL-C.
```
- Run `./leh django createsuperuser` to create admin user. Then you can log in to the Django admin `localhost:8000/admin`.
- It is recommended to stop the container by running `./leh stop`.

# Tips

- Install Python libs by adding it to `requirements.txt` in proper format instead of running `pip install`.
- Run `./leh` for shell command helper. `leh` is a developer-friendly shell script with some commonly-used commands. Currently django commands can only run using `leh`.
- You may need to clean dangling images in docker from time to time. They are usually marked as `<none>`.

---

__*: APIs that need auth token in the headers e.g. `{ Authorization: 'Token xxxxxxxxx' }`__

__[function]: [endpoint] [method] [[payload] [comment]]__

# Auth API

- Sign in: `/api/auth/signin/` POST `{ username: 'ece@gmail.com', password: '12345678' }`
- *Sign out: `/api/auth/signout/` POST 
- Sign up: `/api/auth/signup/` POST `{ username: ece, email: ece@gmail.com, password: '12345678' }`
- *Change password: `/api/auth/change_password/` POST `{ old_password: '12345678', new_password: '12345678' }`

# User API

- *Get current user: `/api/users/` GET
- *Update current user (including address): `/api/users/` PATCH `{ username: 'asdasddasd', shipping_address: { full_name: 'asd', phone_number: '1234567890', email: 's@a.com', address: '1 John St', province: 'ON', postal_code: 'M2W2W2' }}` Do not use this for changing password
<!-- - *Get user address: `/api/users/address/` GET
- *Create/update user address: `/api/users/address/` PUT `{ full_name: 'asd', phone_number: '1234567890', email: 's@a.com', address: '1 John St', province: 'ON', postal_code: 'M2W2W2' }` -->

# Product API

- Retrieve product lists: `/api/products`
- Retrieve product by product id: `/api/products?id=<id>`
- Search products by product name (full text search allowed): `/api/products?name=<name/part-of-the-name>`
- Retrieve product by category: `/api/products?category=<category>`

# Recipe API

- Retrieve recipe lists: `/api/recipes`
- Retrieve recipe by recipe id: `/api/recipes?id=<id>`
- Search recipe by recipe name (full text search allowed): `/api/recipes?name=<name/part-of-the-name>`
- Retrieve recipe by cuisine: `/api/recipes?cuisine=<cuisine>`

# Cart API (current user)

- *Retrieve cart items: `/api/cart/` GET
- *Create new item(s): `/api/cart/` POST `[{ product_id: 1, quantity: 1 }, { product_id: 2, quantity: 1 }]`
- *Update an item: `/api/cart/<item_id>/` PATCH `{ quantity: 2 }` Use this with `{ quantity: 0 }` to remove cart item.
- *Clear cart: `/api/cart/` DELETE

# Order API (current user)

- *Retrieve orders: `/api/orders/` GET
- *Retrieve an order: `/api/orders/<order_id>/` GET
- *Create new order: `/api/orders/` POST `{ status: 'unpaid', order_items: [{ product_id: 1, quantity: 2 }, { product_id: 2, quantity: 1 }] }`
- *Update an order: `/api/orders/<order_id>/` PATCH `{ status: 'cancelled' }` Currently regard `status=cancelled` as deleting order

# Selenium System Test
- Selenium system tests (**@tag(selenium-system)**):
    1. user signup => user login => add shipping address => change shipping address
    2. user signup => user login => search for a product => add it to cart => add address => place order
- To run selenium system tests:
    1. remove all existing L'EH-related running containers 
    2. `docker-compose -f docker-compose.selenium.yml run --name app --rm app python3 manage.py test --teg=selenium-system`
    3. `docker-compose -f docker-compose.selenium.yml down`
- Each selenium system test should be placed in a separate test file to avoid driver error.