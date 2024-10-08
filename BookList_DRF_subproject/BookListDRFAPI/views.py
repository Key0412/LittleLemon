from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Regular routes - function based view
# Easy to implement, readale, easy to use with decorators, quick once-off solution
# @api_view(['GET', 'POST']) # change the parameter of the decorator to allow other HTTP methods
# def books(request):
#     return Response({'message':'list of books'}, status=status.HTTP_200_OK)

# Routing to a class method
class Orders():
    @staticmethod
    @api_view(['GET', 'POST'])
    def listOrders(request):
        return Response({'message':'list of orders'}, status=status.HTTP_200_OK)

# Routing class-based views
# class-based views: less code, less duplication, extend and add features, define specific methods for HTTP request types
class BookView(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if author:
            return Response({"message":"list of the books by " + author}, status.HTTP_200_OK)
        return Response({'message':'list of books'}, status=status.HTTP_200_OK)
    def post(self, request):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
    def put(self, request):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)

class Book(APIView):
    def get(self, request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
    
# Routing classes that extend viewsets
class BookViewset(ViewSet):
    #There are also: ModelViewSet, ReadOnlyModelViewSet, and generics (which has several viewsets)
    # these also need 'queryset' and 'serializer' methods
    
    # you can also override defautl behaviour of default methods by overriding the default functions.
    
    # Defining authentication
    permission_classes = [IsAuthenticated] # will return "detail": "Authentication credentials were not provided."
    def get_permissions(self): # use this to enable authentication selectively
        permission_classes = []
        if self.request.method != 'GET': # this enables authentication for all methods but GET
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    # to return items for authenticated user only you need to override the get_queryset method
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     return Order.objects.all().filter(user=self.request.user)
    
    
    # Default functions to implement CRUD business logic
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