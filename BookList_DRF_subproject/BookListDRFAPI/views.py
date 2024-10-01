from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
# Create your views here.

# Regular routes
@api_view(['GET', 'POST']) # change the parameter of the decorator to allow other HTTP methods
def books(request):
    return Response({'message':'list of books'}, status=status.HTTP_200_OK)

# Routing to a class method
class Orders():
    @staticmethod
    @api_view(['GET', 'POST'])
    def listOrders(request):
        return Response({'message':'list of orders'}, status=status.HTTP_200_OK)

# Routing class-based views
class BookView(APIView):
    def get(self, request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
    
# Routing classes that extend viewsets
class BookViewset(ViewSet):
    def list(self, request):
        return Response({"message":"All books"}, status.HTTP_200_OK)
    def create(self, request):
        return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        return Response({"message":"Deleting a book"}, status.HTTP_200_OK)