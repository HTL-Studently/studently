# WEBSERVER
FROM node:lts
WORKDIR /app

COPY . .

# Install Deno
RUN curl -fsSL https://deno.land/x/install/install.sh | sh

RUN npm install
RUN npm install sharp
RUN npm run build

ENV HOST=0.0.0.0
ENV PORT=4321

EXPOSE 4321

CMD node ./dist/server/entry.mjs