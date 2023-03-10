FROM node

WORKDIR /app

EXPOSE 8080

COPY package.json /app/package.json

RUN npm install

RUN npm install -g @vue/cli

ENV PATH /app/node_modules/.bin:$PATH

COPY . /app

#ENV NODE_ENV=development

#RUN npm run build

CMD ["npm", "run", "serve"]
