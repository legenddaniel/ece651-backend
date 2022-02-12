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

# Product API

- Retrieve product lists: `localhost:8000/api/products`
- Retrieve product by product id: `localhost:8000/api/products?id=<id>`
- Search products by product name (full text search allowed): `localhost:8000/api/products?name=<name/part-of-the-name>`
- Retrieve product by category: `localhost:8000/api/products?category=<category>`

# Recipe API

- Retrieve recipe lists: `localhost:8000/api/recipes`
- Retrieve recipe by recipe id: `localhost:8000/api/recipes?id=<id>`
- Search recipe by recipe name (full text search allowed): `localhost:8000/api/recipes?name=<name/part-of-the-name>`
- Retrieve recipe by cuisine: `localhost:8000/api/recipes?cuisine=<cuisine>`