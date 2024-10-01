from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

urlpatterns = [
    # Regular routes
    path('books', views.books),
    
    # Routing to a class method
    path('orders', views.Orders.listOrders),
    
    # Routing class-based views
    path('books/<int:pk>', views.BookView.as_view()),
    
    # Routing classes that extend viewsets
    # path('books-viewset', views.BookViewset.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         })
    #      ),
    # path('books-viewset/<int:pk>',views.BookViewset.as_view(
    #     {
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'patch': 'partial_update',
    #         'delete': 'destroy',
    #         })
    #      )
    ]

# Routing with SimpleRouter class in DRF
# - it automatically linkts urls to the methods by name convention
router = SimpleRouter(trailing_slash=False)
router.register('books-viewset', views.BookViewset, basename='books-viewset')
urlpatterns += router.urls

# Routing with DefaultRouter class in DRF
# - it automatically linkts urls to the methods by name convention
# - it shows a list of all the available endpoints in the /api/ endpoint
# router = DefaultRouter(trailing_slash=False)
# router.register('books-viewset', views.BookViewset, basename='books-viewset')
# urlpatterns += router.urls