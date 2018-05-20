# IT CROWD Test Interview

This is a test project to show abilities in Python, Django and Rest apis:
The Main Idea is to create a rest api interface for CRUD movies information.
relating Persons with Movies, persons will be the directors, actors and producers of movies:

* The content (Movies an Persons) can only be added/updated/deleted if User is logged in.
* The content can be obtained with out being logged in
* The authentication system is built using JWT tokens

The project is deployed in AWS , and can be accessed using the following url:
http://ec2-34-226-248-137.compute-1.amazonaws.com/

Django Admin can be accessed using:
username: admin
password: qwerty12345

at http://ec2-34-226-248-137.compute-1.amazonaws.com/admin/

Generated docs can be found:
http://ec2-34-226-248-137.compute-1.amazonaws.com/docs/


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
curl -X POST http://ec2-34-226-248-137.compute-1.amazonaws.com/movies/ -d '{"release_year": 2020, "title": "The Great Stoner Rock Movie", "actors": [2], "producers": [2], "directors": [1, 2]}' -H 'Content-Type: application/json' -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJfaWQiOjEsImV4cCI6MTUyNjg0MzgzMiwidXNlcm5hbWUiOiJhZG1pbiJ9.T5_Q4-_X9kmWKSkhfWoZGiBQnQhqGeLtxMr0-E5fyMo'

{
  "id": 1,
  "title": "The Great Stoner Rock Movie",
  "release_year": 2020,
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
        "The Great Stoner Rock Movie(2020)"
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
        "The Great Stoner Rock Movie(2020)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(2020)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(2020)"
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
        "The Great Stoner Rock Movie(2020)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(2020)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(2020)"
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
        "The Great Stoner Rock Movie(2020)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(2020)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(2020)"
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
  "release_year": 2020,
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
        "The Great Stoner Rock Movie(2020)"
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
        "The Great Stoner Rock Movie(2020)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(2020)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(2020)"
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
        "The Great Stoner Rock Movie(2020)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(2020)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(2020)"
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
        "The Great Stoner Rock Movie(2020)"
      ],
      "produced": [
        "The Great Stoner Rock Movie(2020)"
      ],
      "acted": [
        "The Great Stoner Rock Movie(2020)"
      ]
    }
  ]
}
```


Content information can be obtained without being logged in:
```
curl -X GET http://ec2-34-226-248-137.compute-1.amazonaws.com/movies/1/ -H 'Content-Type: application/json'

{
  "id": 1,
  "title": "The Great Stoner Rock Movie",
  "release_year": 2020,
    .
    .
    .
}
```

Content can be deleted if user is logged in:
```
curl -X DELETE http://ec2-34-226-248-137.compute-1.amazonaws.com/movies/1/ -H 'Content-Type: application/json' -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJfaWQiOjEsImV4cCI6MTUyNjg0MzgzMiwidXNlcm5hbWUiOiJhZG1pbiJ9.T5_Q4-_X9kmWKSkhfWoZGiBQnQhqGeLtxMr0-E5fyMo'
```

The technologies used here are:
* Django: Framework for creating web services
* Django Rest Framework: Framework used to create rest apis interfaces
* Django rest JWT: Jwt  implementation for rest framework, used for authentication. For more info about jwt: https://jwt.io/introduction/
* Sqlite: As there is no Database restriction we use sqlite that works great for small projects like this

