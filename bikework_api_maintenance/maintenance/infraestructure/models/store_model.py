from django.db import models

class Store(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'bikewkdate"."store'

    def __str__(self):
        return self.name
