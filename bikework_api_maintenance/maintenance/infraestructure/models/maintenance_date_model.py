from django.db import models

from maintenance.infraestructure.models.customer_model import Customer
from maintenance.infraestructure.models.store_model import Store

class MaintenanceDate(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField()
    hour = models.SmallIntegerField()
    maintenance_type = models.CharField(max_length=255)
    staff = models.CharField(max_length=255, null=True, blank=True)

    customer_document_type = models.CharField(max_length=10, null=True, blank=True)
    customer_document_number = models.CharField(max_length=50, null=True, blank=True)
    customer = models.ForeignKey(
        Customer,
        to_field='document_number',
        on_delete=models.SET_NULL,
        db_column='customer_document_number',
        related_name='maintenance_dates',
        null=True,
        blank=True,
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        db_column='store_id',
        related_name='maintenance_dates'
    )

    class Meta:
        db_table = 'maintenance_date'
        indexes = [
            models.Index(fields=['customer_document_type', 'customer_document_number']),
            models.Index(fields=['store']),
        ]

    def __str__(self):
        return f'Maintenance {self.id} on {self.date} at hour {self.hour}'