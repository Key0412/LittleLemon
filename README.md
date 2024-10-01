# Meta API course - LittleLemon API

[Course link](https://www.coursera.org/learn/apis/)  
[Django documentation](https://docs.djangoproject.com/en/5.1/)

## Commands to setup the Django project

```
# Get python image
docker pull python
# Create container from image 
docker run -dit --name <container_name> [options] python
# optionally map paths from OS to container: -v <OS path>:<container path> 

# start container
docker start <container_name>
# access bash
docker exec -it <container_name> bash
```

```
# Install django
python -m pip install Django 
# start a project
django-admin startproject Littlelemon .
# start the app
python manage.py startapp LittlelemonAPI
# run a server in port 8000
python manage.py runserver
# change default port to 9000
python manage.py runserver 9000
```

#### extra: recurrent configurations
- add APP to project's settings INSTALLED_APPS
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BookListAPI',
]

```
* create models inside models.py
```
class Book(models.Model):
    title = models.CharField(max_length=255)
        author = models.CharField(max_length=255)
        price = models.DecimalField(max_digits=5,decimal_places=2)

        class Meta:
            indexes = [
                models.Index(fields=["price"]),
            ]
```
* register models inside admin.py
```
admin.site.register(Book)
```
- create migration with makemigrations
- execute migrate command to apply changes to the database
```
python manage.py makemigrations
python manage.py migrate
```
* create superuser to access admin page
```
python manage.py createsuperuser
```
* add url.py file to the APP folder. add urlpatterns/routes.
```
from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books)
]
```
* import API url paths to the project paths in url.py
```
path('api/', include('BookListAPI.urls')),
```
* modify the views file. e.g. add a view for books.
```
from django.shortcuts import render
from django.db import IntegrityErrorexception 
from django.http import JsonResponsefunction 
from .models import Book # import our Book db model
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

@csrf_exempt
def books(request):
    if request.method == 'GET':
        ···
```


## Tools

* [Insomnia](https://insomnia.rest/): REST API client used to store, organize, and execute REST API requests.
* [Postman](https://www.postman.com/): REST API development framework to make HTTP requests, store, test, debug.
    * [Postman-echo](https://www.postman.com/postman/published-postman-templates/documentation/ae2ja6x/postman-echo?ctx=documentation
    ):service you can use to test your REST clients and make sample API calls. 
* [Curl](https://curl.se/): allows making HTTP requests.
* [httpbin.org](https://httpbin.org/): Request and Response Service httpbin.org. Httpbin.org is an open-source web service that allows you to make HTTP calls without any additional installations or dependencies. 
* [httpie](https://httpie.io/): open-source API testing
* [Django](https://www.djangoproject.com/): high-level Python web framework that encourages rapid development and clean, pragmatic design. 
* [HTTP reesponse status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* Mock API data generators and Mock API endpoints: A mock API imitates the real API endpoint with fake data so that the client application developers can start development before the actual API is developed.
    * [Mockaroo data generator](https://www.mockaroo.com/)
    * [Mockapi mock api endpoints](https://mockapi.io/)


## REST APIS

Scalable, Flexible, Independent.

Restfull:
* Server-client architecture
* Stateless
* Cache Capacity
* Layered
* Uniform
* Code on demand

### Best practices:
* KISS - keep it simple stupid: One API - One task.
* Filter, Order, and Paginate: filter large result sets and sort them. Api should be capable of filtering results.Show only a certain number of items per page.
* Versioning: in general, support only two versions of any given resource.
* Caching: always implement caching and send relevant http headers in response. Minimize number of calls client makes to API.
* Rate limiting: rate limiting to prevent abuse of the API.
* Monitoring: Monitor status codes, response times, and network bandwith.

API Security:
* SSL: secure socket layer. encrypts data on transit, allows HTTPS.
* Signed URLS: limits access to a resource for a limited time. Clients need a signature to access data:
    * HMAC: a popular signing mechanism used by modern applications
* Authentication: token-based authentication. (HTTP authentication requires username and password everytime and it is less safe). To create token one can use ad hoc policy for the backend framework or industry standard JSON Web Token (JWT). During authentication there are important HTTP codes:
    * 401 - unauthorized. username and password don't match
    * 403 - forbidden. user is not allowed
* Cross-Origin Resource Sharing CORS policy and server firewalls. Limits the 3d party and IP addresses that can access your API.

### Access control:
* Role: each role has a collection of well defined privileges that authorize them to perform tasks. Authentication != Authorization.
    * During authentication, the API web server checks the clients' access token or username/password, and provides her with an access token for the following requests.
    * During requests, the authorization layer checks if the client is authorized to perform the action.
* The Django admin panel provides support for the creation of roles (groups) and for privileges managemnt based on the django projects' models.

## DRF - django rest framework

DRF is a toolkit built on top of the Django web framework. It comes with many helpful utility classes and objects that can help developers build robust APIs quickly.  
* Easy to integrate with plain django
* we browsable API for quick experiments
* Flexible request and response processing
* Human readable HTTP status codes
* Built-in view set classes make it easy to create a functional CRUD
* Built-in serializers. Data model <-> Native python datatypes.
* Support for authentication. Enable social connections.

Guide: [DRF in a container](https://pradeepc.hashnode.dev/django-rest-framework-1-dockerize-your-project)

To install DRF:
```
pip install djangorestframework
```
To use it in your Django project, go to your projects' settings in `settings.py` and append *'rest_framework'* to the list.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BookListAPI',
    'rest_framework'
]
```

The `@api_view` decorator is one of the most important on DRF. It allows defining which HTTP methods a view accepts, it turns the API request into an organized browseable page with request information, it provides a way to implement throtling and rating, and authentication.