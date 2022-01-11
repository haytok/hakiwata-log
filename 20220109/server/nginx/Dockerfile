FROM nginx:alpine

COPY ./nginx/conf/default.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]
