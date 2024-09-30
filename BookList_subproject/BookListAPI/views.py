from django.shortcuts import render
from django.db import IntegrityError # exception in Django, a web framework for Python, raised when there is a violation of the database integrity constraints.
from django.http import JsonResponse # JsonResponse is a subclass that helps us to create a JSON-encoded response
from .models import Book # import our Book db model
from django.views.decorators.csrf import csrf_exempt # Mark a view function as being exempt from the CSRF view protection - turn off this protection
from django.forms.models import model_to_dict # Return a dict containing the data in instance suitable for passing as a Form's initial keyword argument.

# Create your views here.

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = { 'books': list( Book.objects.all().values() ) }
        return JsonResponse(books, status=200)
        
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        book = Book(title=title, author=author, price=price, inventory=inventory)
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'}, status=400)
        return JsonResponse(model_to_dict(book), status=201)
        