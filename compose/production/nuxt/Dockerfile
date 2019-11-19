FROM node:latest as builder

WORKDIR /app

COPY ./client/package.json /app/package.json
COPY ./client/package-lock.json /app/package-lock.json

RUN npm install

COPY ./client /app

RUN npm run build

RUN rm -rf node_modules && \
  NODE_ENV=production npm install

FROM node:alpine

WORKDIR /app

COPY --from=builder /app  .

ENV HOST 0.0.0.0

CMD [ "npm", "start" ]
