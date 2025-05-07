from django.urls import path
from maintenance.presentation.maintenance_date_view import MaintenanceDateView
from maintenance.presentation.views import CustomerView
from maintenance.presentation.health_views import HealthCheckView

urlpatterns = [
    # Rutas relacionadas con clientes
    path("customers/", CustomerView.as_view(), name="customer"),
    
    # Rutas relacionadas con el estado de salud
    path("health/", HealthCheckView.as_view(), name="health_check"),

        # Rutas relacionadas con el estado de salud
    path("maintenance/", MaintenanceDateView.as_view(), name="maintenance_date"),
]
