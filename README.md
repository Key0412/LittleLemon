# Meta API course - LittleLemon API

Course link: https://www.coursera.org/learn/apis/lecture/sn2Ez/create-a-django-project-using-pipenv  
Django documentation: https://docs.djangoproject.com/en/5.1/

## Commands to setup the Django project

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

extra APP and config:

```
# 0 - add APP to project's settings INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BookListAPI',
]
# 1 - create models inside models.py
class Book(models.Model):
    title = models.CharField(max_length=255)
        author = models.CharField(max_length=255)
        price = models.DecimalField(max_digits=5,decimal_places=2)

        class Meta:
            indexes = [
                models.Index(fields=["price"]),
            ]
# 2 - register models inside admin.py
admin.site.register(Book)
# 3 - create migration with makemigrations - 
python manage.py makemigrations
# 4 - execute migrate command to apply changes to the database -
python manage.py migrate
# 5 - create superuser to access admin page
python manage.py createsuperuser
# 6 - add url.py file to the APP folder. add urlpatterns.
from django.urls import path
from . import views


urlpatterns = [
# Add URL configuration for the path() function here
    path('books', views.books)
]
# 7 - import API url paths to the project paths in url.py
path('api/', include('BookListAPI.urls')),
# 8 - modify the views file. add a view for books
from django.shortcuts import render
from django.db import IntegrityErrorexception # exception in Django, a web framework for Python, raised when there is a violation of the database integrity constraints.
from django.http import JsonResponsefunction # JsonResponse is a subclass that helps us to create a JSON-encoded response
from .models import Book # import our Book db model
from django.views.decorators.csrf import csrf_exempt # Mark a view function as being exempt from the CSRF view protection - turn off this protection
from django.forms.models import model_to_dict # Return a dict containing the data in instance suitable for passing as a Form's initial keyword argument.

# Create your views here.

@csrf_exempt
def books(request):
    if request.method == 'GET':
```


## Tools

* Insomnia: REST API client used to store, organize, and execute REST API requests. https://insomnia.rest/
* Postman: REST API development framework to make HTTP requests, store, test, debug. https://www.postman.com/
    * Postman-echo:service you can use to test your REST clients and make sample API calls. https://www.postman.com/postman/published-postman-templates/documentation/ae2ja6x/postman-echo?ctx=documentation

* Curl: allows making HTTP requests. https://curl.se/
* httpbin.org: https://httpbin.org/. Request and Response Service httpbin.org. Httpbin.org is an open-source web service that allows you to make HTTP calls without any additional installations or dependencies. 
* httpie: https://httpie.io/. open-source API testing
* Django: high-level Python web framework that encourages rapid development and clean, pragmatic design. https://www.djangoproject.com/
* HTTP reesponse status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

## REST APIS

Scalable, Flexible, Independent.

Restfull:
* Server-client architecture
* Stateless
* Cache Capacity
* Layered
* Uniform
* Code on demand

Best practices:
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

Acess control:
* Role: each role has a collection of well defined privileges that authorize them to perform tasks. Authentication != Authorization.
    * During authentication, the API web server checks the clients' access token or username/password, and provides her with an access token for the following requests.
    * During requests, the authorization layer checks if the client is authorized to perform the action.
* The Django admin panel provides support for the creation of roles (groups) and for privileges managemnt based on the django projects' models.