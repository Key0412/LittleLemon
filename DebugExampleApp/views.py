from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display_even_numbers(request):
    response = ""
    for i in range(1, 10):
        remainder = i%2
        if not remainder:
            response += str(i) + "<br/>"
    return HttpResponse(response)