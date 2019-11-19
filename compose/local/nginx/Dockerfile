FROM nginx:1.17.5

COPY ./compose/local/nginx/templates/nginx.conf /templates/

COPY ./compose/local/nginx/entrypoint /entrypoint
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]

CMD [ "nginx", "-g", "daemon off;"]
