from django.db import models

class Customer(models.Model):
    document_type = models.CharField(max_length=10)
    document_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        db_table = '"."customer'
        unique_together = ('document_type', 'document_number')

    def __str__(self):
        return f"{self.full_name} ({self.document_type}-{self.document_number})"