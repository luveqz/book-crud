FROM nginx:1.17.5

RUN apt-get update
RUN apt-get install -y certbot python-certbot-nginx 

COPY ./compose/production/nginx/templates/nginx.conf /templates/

COPY ./compose/production/nginx/entrypoint /entrypoint
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]

CMD [ "nginx", "-g", "daemon off;"]
