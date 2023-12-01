# WEBSERVER
FROM node:lts
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 4321

RUN ["npm", "run", "build"]

CMD ["npm", "start"]