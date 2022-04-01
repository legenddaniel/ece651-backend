FROM node:latest as node
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build --prod
RUN npm install -g @angular/cli

FROM nginx:alpine
COPY --from=node /app/dist/lehstore /usr/share/nginx/html
EXPOSE 4200:80
