# IT CROWD Test Interview

This is a test project to show abilities in Python, Django and Rest apis:
The Main Idea is to create a rest api interface for CRUD movies information.
Relating Persons with Movies, persons will be the directors, actors and producers of movies:

* The content (Movies an Persons) can only be added/updated/deleted if User is logged in.
* The content can be obtained with out being logged in
* The authentication system is built using JWT tokens

The project is deployed in AWS , and can be accessed using the following url:
http://ec2-34-226-248-137.compute-1.amazonaws.com/

Django Admin can be accessed using:
```
username: admin
password: qwerty12345
```

at http://ec2-34-226-248-137.compute-1.amazonaws.com/admin/

Generated docs can be found:
http://ec2-34-226-248-137.compute-1.amazonaws.com/docs/


## Some Examples:

To be able to create content first we need to obtain a JWT token:
```
$ curl -X POST -H 'Content-Type: application/json' http://ec2-34-226-248-137.compute-1.amazonaws.com/api-token-auth/ -d '{"username": "admin", "password": "qwerty12345"}'
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJfaWQiOjEsImV4cCI6MTUyNjg0MzgzMiwidXNlcm5hbWUiOiJhZG1pbiJ9.T5_Q4-_X9kmWKSkhfWoZGiBQnQhqGeLtxMr0-E5fyMo"
}

```

Now with the token we can start creating content:
```
curl -X POST -H 'Content-Type: application/json' -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJfaWQiOjEsImV4cCI6MTUyNjg0MzgzMiwidXNlcm5hbWUiOiJhZG1pbiJ9.T5_Q4-_X9kmWKSkhfWoZGiBQnQhqGeLtxMr0-E5fyMo'  http://ec2-34-226-248-137.compute-1.amazonaws.com/persons/ -d '{"first_name": "Josh", "last_name": "Homme", "aliases": ["Red", "Josh"]}'
{
  "id": 2,
  "first_name": "Josh",
  "last_name": "Homme",
  "aliases": [
    "Red",
    "Josh"
  ],
  "directed": [],
  "produced": [],
  "acted": []
}
```

We can create a movie, we need to have the person's id to be able to add it to a movie:
```
curl -X POST http://ec2-34-226-248-137.compute-1.amazonaws.com/movies/ -d '{"release_year": 2018, "title": "The Great Stoner Rock Movie", "actors": [2], "producers": [2], "directors": [1, 2]}' -H 'Content-Type: application/json' -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJfaWQiOjEsImV4cCI6MTUyNjg0MzgzMiwidXNlcm5hbWUiOiJhZG1pbiJ9.T5_Q4-_X9kmWKSkhfWoZGiBQnQhqGeLtxMr0-E5fyMo'

{
  "id": 1,
  "title": "The Great Stoner Rock Movie",
  "release_year": 'MMXVIII',
  "directors": [
    {
      "id": 1,
      "first_name": "Josh",
      "last_name": "Homme",
      "aliases": [
        "Red",
        "Josh"
      ],
      "directed": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ],
      "produced": [],
      "acted": []
    },
    {
      "id": 2,
      "first_name": "Josh",
      "last_name": "Homme",
      "aliases": [
        "Red",
        "Josh"
      ],
      "directed": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ]
    }
  ],
  "actors": [
    {
      "id": 2,
      "first_name": "Josh",
      "last_name": "Homme",
      "aliases": [
        "Red",
        "Josh"
      ],
      "directed": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ]
    }
  ],
  "producers": [
    {
      "id": 2,
      "first_name": "Josh",
      "last_name": "Homme",
      "aliases": [
        "Red",
        "Josh"
      ],
      "directed": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(MMXVIII)"
      ]
    }
  ]
}
```

The contents( Movies or Persons) can be updated if the user is logged in, using the movie's id:
```
url -X PATCH http://ec2-34-226-248-137.compute-1.amazonaws.com/movies/1/ -d '{"release_year": 2020}' -H 'Content-Type: application/json' -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJfaWQiOjEsImV4cCI6MTUyNjg0MzgzMiwidXNlcm5hbWUiOiJhZG1pbiJ9.T5_Q4-_X9kmWKSkhfWoZGiBQnQhqGeLtxMr0-E5fyMo'

{
  "id": 1,
  "title": "The Great Stoner Rock Movie",
  "release_year": "MMXX",
    .
    .
    .
}
```


Content information can be obtained without being logged in:
```
curl -X GET http://ec2-34-226-248-137.compute-1.amazonaws.com/movies/1/ -H 'Content-Type: application/json'

{
  "id": 1,
  "title": "The Great Stoner Rock Movie",
  "release_year": "MMXX",
    .
    .
    .
}
```

Content can be deleted if user is logged in:
```
curl -X DELETE http://ec2-34-226-248-137.compute-1.amazonaws.com/movies/1/ -H 'Content-Type: application/json' -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJfaWQiOjEsImV4cCI6MTUyNjg0MzgzMiwidXNlcm5hbWUiOiJhZG1pbiJ9.T5_Q4-_X9kmWKSkhfWoZGiBQnQhqGeLtxMr0-E5fyMo'
```


## Techonology

The main technologies used here are:
* Django: Framework for creating web services
* Django Rest Framework: Framework used to create rest apis interfaces
* Django rest JWT: Jwt  implementation for rest framework, used for authentication. For more info about jwt: https://jwt.io/introduction/
* Sqlite: As there is no database restriction we use sqlite that works great for small projects like this.

Packages used:
```
certifi==2018.4.16
chardet==3.0.4
coreapi==2.3.3
coreschema==0.0.4
Django==2.0.5
django-rest-framework==0.1.0
djangorestframework==3.8.2
djangorestframework-jwt==1.11.0
idna==2.6
itypes==1.1.0
Jinja2==2.10
MarkupSafe==1.0
PyJWT==1.6.3
pytz==2018.4
requests==2.18.4
uritemplate==3.0.0
urllib3==1.22
```

## Try it locally

we will need python3 to be able to run it locally:

Install dependencies
```
pip install -r requirements.txt
```

Run migration
```
python manage.py migrate
```

Create a new user
```
python managa.py createsuperuser
```
Run the django test server
```
python manage runserver 0.0.0.0:8000
```
