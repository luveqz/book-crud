FROM node:latest

WORKDIR /

COPY ./client/package.json /package.json
COPY ./client/package-lock.json /package-lock.json

RUN npm install
RUN echo $NODE_ENV

WORKDIR /app

ENV HOST 0.0.0.0

CMD ["/node_modules/.bin/nuxt"]
