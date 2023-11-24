FROM nginx:latest

RUN rm /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/

COPY ./cert/studently.cert /etc/nginx/certs/studently.cert
COPY ./cert/studently.key /etc/nginx/certs/studently.key

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]