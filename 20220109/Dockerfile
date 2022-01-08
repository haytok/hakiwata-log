FROM nginx:alpine

COPY ./conf/default.conf /etc/nginx/conf.d/
RUN mkdir etc/nginx/html
RUN echo Hello > etc/nginx/html/index.html

CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]
