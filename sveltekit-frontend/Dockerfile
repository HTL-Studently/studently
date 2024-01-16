FROM node:latest

WORKDIR /app

COPY node_modules .
COPY package.json . 
COPY package-lock.json .

COPY . .

ENV HOST = 0.0.0.0
ENV PORT = 3000


RUN npm ci --omit dev
RUN node build

EXPOSE 5000

