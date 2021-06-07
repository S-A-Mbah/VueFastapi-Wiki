#Build front end

FROM node:lts-alpine as vue-build

RUN mkdir -p /app

WORKDIR /app

COPY package*.json ./

RUN yarn install

COPY . .

#RUN yarn add @vue/cli

RUN ./node_modules/.bin/eslint --fix ./src

RUN  yarn run build

EXPOSE 8080

CMD [ "yarn", "start" ]

#
#Build Backend
#
FROM python:3 as fastapi-build
WORKDIR /app/src/api
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
#RUN uvicorn main:app --reload
#CMD ["main.py"]
EXPOSE 8000
#ENTRYPOINT ["python3"]

#Nginx
FROM nginx:stable-alpine as production-stage

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=fastapi-build /app/src/api/ /usr/share/nginx/html

COPY --from=vue-build /app/dist /usr/share/nginx/html

ENTRYPOINT ["nginx", "-g", "daemon off;"]
