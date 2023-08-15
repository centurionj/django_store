FROM nginx:1.21

RUN rm /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/nginx/conf.d

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY ./static /app/static
