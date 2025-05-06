from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    

    class Meta:
        db_table = "customer"