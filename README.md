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

# Cart API

- *Retrieve cart items: `/api/cart/` GET
- *Create new item: `/api/cart/` POST `{ product: 2, quantity: 1 }` (product -> product_id)
- *Update an item: `/api/cart/<item_id>/` PATCH `{ quantity: 2 }` Wse this with `{ quantity: 0 }` to remove cart item.
- *Clear cart: `/api/cart/` DELETE