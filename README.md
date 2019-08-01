# Flask Boilerplate 4Geeks Academy

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io#https://github.com/4GeeksAcademy/flask-rest-hello.git)

## How to stat the project?

There is an example API working with an example database. All your application code should be written inside the `./src/` folder.

- src/main.py (it's were your endpoints should be coded)
- src/mode.py (your database tables and serialization logic)
- src/utils.py (some reusable classes and functions)

For a more detailed explanation look for the tutorial inside the `docs` folder.

## Remember migrate every time you change your models

You have to migreate and upgrade the migrations for every update your make to your models:
```
$ pipenv run migrate (to make the migrations)
$ pipenv run upgrade  (to update your databse with the migrations)
```


## Instalation for ubuntu

1. Make sure you have python 3.6+
```sh
$ pipenv install (to install pip packages)
$ pipenv run migrate (to create the database)
$ pipenv run start (to start the flask webserver)
```


## Deploy your website to heroku

This template is 100% compatible with heroku, just make sure to understand and execute the following steps

1. Install heroku
```sh
$ npm i heroku -g
```

2. Login to heroku on the command line
```sh
$ heroku login -i
```
3. Create an application (if you don't have it already)
```sh
$ heroku create <your_application_name>
```
4. Commit and push to heroku
Make sure you have commited your changes and push to heroku
```sh
$ git push heroku master
```

# PET HUNTER API

### USERS

1. POST `/users`

```
BODY:

{ username: "", mail: "",  password: ""}


RESPONSE:

{
    "result": "ok"
}
```


2. GET `/users`

```
RESPONSE:

[
    { username: "", mail: "",  password: "", userid:int}
    { username: "", mail: "",  password: "", userid:int}
    { username: "", mail: "",  password: "", userid:int}
    { username: "", mail: "",  password: "", userid:int}...
]
```


### USERS/USER_ID

1. PUT `/users/userid`

```
BODY:

{ field: ""}


RESPONSE:

{ username: "", mail: "",  password: ""}, 200
```

2. GET `/users/userid`

```
RESPONSE:

[
    { username: "", mail: "",  password: ""}
]
```

3. DELETE `/users/userid`

```
RESPONSE:

{
    "result": "ok"
}
```
### USERS/LOGIN

1. POST `/users/login`
```
BODY:

{ mail: "",  password: ""}


RESPONSE:

{ result: true, id: int} or { result: false}
```
### POSTS

1. GET `/posts`

```
RESPONSE:

[
    { userid:int, postid:int, date: date, status:"", dogname:"", size:"", breed:"", description:"", location:"",},
    { userid:int, postid:int, date: date, status:"", dogname:"", size:"", breed:"", description:"", location:"",},
    { userid:int, postid:int, date: date, status:"", dogname:"", size:"", breed:"", description:"", location:"",}
]
```
2. POST `/posts`

```
BODY:
{ userid:int, status:"", dogname:"", size:"", breed:"", description:"", location:"",}

RESPONSE:

{ result: "ok"}
```

### POSTS/POSTID

1. PUT `/posts/postid`

```
BODY:

{ field: ""}


RESPONSE:

{ userid:int, postid:int, date: date, status:"", dogname:"", size:"", breed:"", description:"", location:"",}, 200
```

2. GET `/posts/postid`

```
RESPONSE:

{ userid:int, postid:int, date: date, status:"", dogname:"", size:"", breed:"", description:"", location:"",}

```

3. DELETE `/posts/postid`

```
RESPONSE:

{
    "result": "ok"
}
```

otros:

duda en consultas query y respuesta. es con post?, para login, search, posts de un usuario