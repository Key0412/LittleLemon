from django.db import models

# Create your models here.
class Book(models.Model):
    # A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

    # The basics:

    # Each model is a Python class that subclasses django.db.models.Model.
    # Each attribute of the model represents a database field.
    # With all of this, Django gives you an automatically-generated database-access API;
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    inventory = models.IntegerField(default=0)
    
    class Meta: # Give your model metadata by using an inner class Meta, like so:
        indexes = [
            models.Index(fields=["price"]),
        ] # Index classes ease creating database indexes.
        
# 0 - add APP to project's settings INSTALLED_APPS
# 1 - create model inside models.py
# 2 - register model inside admin.py
# 3 - create migration with makemigrations - python manage.py makemigrations
# 4 - execute migrate command to apply changes to the database - python manage.py migrate