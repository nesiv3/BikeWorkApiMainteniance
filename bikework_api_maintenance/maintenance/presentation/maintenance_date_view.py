# views/maintenance_date_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from maintenance.application.commands.create_maintenance_date import CreateMaintenanceDateCommand
from maintenance.application.queries.get_all_maintenance_dates import GetAllMaintenanceDatesQuery
from maintenance.application.interfaces.mediator import Mediator
from maintenance.application.handlers.create_maintenance_date_handler import CreateMaintenanceDateHandler
from maintenance.application.handlers.get_all_maintenance_dates_handler import GetAllMaintenanceDatesHandler
from maintenance.infraestructure.unit_of_work import UnitOfWork
from maintenance.infraestructure.repositories.maintenance_date_repository import MaintenanceDateRepository

class MaintenanceDateView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        uow = UnitOfWork(maintenance_date_repository=MaintenanceDateRepository())
        self.mediator = Mediator()
        self.mediator.register(CreateMaintenanceDateCommand, CreateMaintenanceDateHandler(uow))
        self.mediator.register(GetAllMaintenanceDatesQuery, GetAllMaintenanceDatesHandler(uow))

    def get(self, request):
        query = GetAllMaintenanceDatesQuery()
        result = self.mediator.send(query)
        serialized = [r.__dict__ for r in result]
        return Response(serialized)

    def post(self, request):
        data = request.data
        try:
            command = CreateMaintenanceDateCommand(
                date=data.get("date"),
                hour=data.get("hour"),
                maintenance_type=data.get("maintenance_type"),
                staff=data.get("staff"),
                customer_document_number=data.get("customer_document_number"),
                customer_document_type=data.get("customer_document_type"),
                store_id=data.get("store_id")
            )
            self.mediator.send(command)
            return Response({"message": "Created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
