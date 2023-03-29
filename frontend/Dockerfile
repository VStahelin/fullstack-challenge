FROM node:15.12.0

WORKDIR /app

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ADD . .

RUN npm install

ENTRYPOINT ["/docker-entrypoint.sh"]

