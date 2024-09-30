# Meta API course - LittleLemon API

Course link: https://www.coursera.org/learn/apis/lecture/sn2Ez/create-a-django-project-using-pipenv

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
* Role: each role has a collection of well defined privileges that authorize them to perform tasks.