# Back
## lunch terminal
### Install dependencies
```
pip install --no-cache-dir -r requirements.txt
```
### lunch back-end
```
uvicorn main:app --reload
```

# front
## lunch new terminal
## Project setup
```
yarn install
```
### Lints and fixes files
```
./node_modules/.bin/eslint --fix ./src
```
### Compiles and hot-reloads for development
```
yarn serve
```
### Compiles and minifies for production
```
yarn build
```

#Nginx
## lunch new terminal
### Build Docker
```
sudo docker build --tag md-wiki:2021 .
```
### Run Docker Container
```
sudo docker run --name vuefastapi -ti -p 8080:8080 md-wiki:2021
```
### 
```
sudo docker exec -t vuefastapi bash -c uvicorn main:app --reload
```
