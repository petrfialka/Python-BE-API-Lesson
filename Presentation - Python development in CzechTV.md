---
theme: white
margin: "0.2"
---
# Python 
# at
# CzechTV
---
## Introduction
### Who am I?
---

## Petr Fialka
- Technological enthusiast
- Software Engineer
- Programming Polyglot (but mainly Python and Node.js)

---

## Petr Fialka
### (at Czech Television)
- Chapter Lead for Python and Node.js

---

## Petr Fialka
## (at Czech Television)
- ~~Chapter Lead for Python and Node.js~~
- Head of Developmet at CzechTV

---
### Who are you?
#### Game - raise your hand if
---

You know Python.

---

You ever worked on Rest API.

---

You know what GraphQL is.

---

You know about microservices.

---

You know Docker.

---

You want 5 minute break in middle of lesson.

---

You want full lesson in one go.

---

Thank you.

---
## Python REST API frameworks (open-source)
- [FastAPI](https://fastapi.tiangolo.com/) - [GitHub](https://github.com/fastapi/fastapi)
- [Django](https://www.djangoproject.com/) - [GitHub](https://github.com/django/django)
- [Flask](https://flask.palletsprojects.com/en/stable/) - [GitHub](https://github.com/pallets/flask)
---
## FastAPI
- Type hints first - documentation driven ([Swagger](https://swagger.io/)) out of box
- Focused on backend development
- Built on starlette and pydantic (high-performance)
- **Outstanding DX** (developer expirience)
- Missing "native" ORM ([SQL model](https://sqlmodel.tiangolo.com/) in works)
- Async 😍
---
## Django
- Full stack framework (batteries included)
- Can be backend focused (Django Rest Framework - [DRF](https://www.django-rest-framework.org/))
- Django-core has good stability policy (changes are introduced very slowly)
	- Could be negative
- Secret sauce around Django is hidden all over web (Django Ninja, serpy, ...)
- Django ORM
- Can't be used for backend development out of box (needs some work)
- Sync 😵 (But there is hope)
---
## Flask
- Could be considered full stack framework
- Is lightweight (very)
	- So you need to install batteries yourself
- Can be backend focused ([Flask RESTful](https://flask-restful.readthedocs.io/en/latest/))
- Sync 😵 (But there is [Quart](https://quart.palletsprojects.com/en/latest/))
---
## Honorable mentions
- [Falcon](https://falcon.readthedocs.io/en/stable/)
	- CT24 was running partialy on Falcon until last week
- [Django Ninja](https://django-ninja.dev/)
	- Notice similarities with FastAPI
	- "Cool child of Django and FastAPI"
- [PyNest](https://github.com/PythonNest/PyNest)
	- Solves dependency injection issues of FastAPI
	- Built on top of FastAPI
	- Inspired by popular javascript framework Nest.js
---
## (CODING) Let's code some backend
- Use of Django
- CT Book Library (you borrow books there)
	- Book management
		- New book
		- Edit book
		- Get books (filters)
		- Get 1 book by ID
	- Borrow management
		- Is book available?
		- Who has it?
---
## Microservices
Clever way to scale your application.

---
## Microservices
~~Clever way to scale your application.~~

Clever way to scale you application together with your problems and also introducing new ones.
- [Docker](https://www.docker.com/)
- docker-compose
- [Kubernetes](https://kubernetes.io/) (k8s)
- Integration Testing
- Documentation
---
## Docker
- These days you can't live without it
- Container vs. Virtual Machine
- Docker wraps your application into "standardized runtime"
- Phrase "It works on my machine" is less heard after introduction of docker (but not completely eliminated)
---
## Docker Compose
- Running multi-container applications
---
### (CODING) Let's split our application to microservices and dockerize it
- Split book management from borrow management
- Run it with docker
- Use API gateway
- Testing
---
## Python GraphQL
- [GraphQL? Whaat?](https://graphql.org/)
- [Graphene](https://graphene-python.org/) - [GitHub](https://github.com/graphql-python/graphene)
- [Strawberry](https://strawberry.rocks/) - [GitHub](https://github.com/strawberry-graphql/strawberry.rocks)
- [Ariadne](https://ariadnegraphql.org/) - [GitHub](https://github.com/mirumee/ariadne)
---
## GraphQL
- Different approach to backend development and data delivery definition
- Defines a Query Language (QL)
- Documented and typed interface out of box
- Missing some key features in standard
	- Input union for example (in works)
- There are two different approaches to defining interface
	- Schema (SDL) first
	- Code first
- Again - introducing several new problems you have to battle with
	- N+1 problem (Dataloaders)
	- Database connection is heavy on creating sessions (DB Pooling)
	- Learning curve of GQL is hard
	- GraphQL Federation
	- Possible vendor lock (with Apollo GraphQL 💲💲💲- it can eat your wallet)
---
## Graphene
- Object First approach to defining schema
- Inheritance heavy
- Itegration on Django ORM or SQLAlchemy
---
## Strawberry
- Object First approach to defining schema
- Decorators heavy
---
## Ariadne
- Schema First
- Raw GQL expirience
- Support for GQL Federation
---
## Microservices Revisited with GraphQL
### Federated GraphQL
Code time!
---
## Necessary evil in development
- Security
- Documentation
- Code Quality
- Testing
	- Function
		- Unit Testing
		- Integration Testing
	- Non-function
		- Performance