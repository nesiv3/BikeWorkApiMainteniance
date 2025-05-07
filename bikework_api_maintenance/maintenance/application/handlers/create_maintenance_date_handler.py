# application/handlers/create_maintenance_date_handler.py

from maintenance.domain.entities.maintenance_date_entity import MaintenanceDate
from maintenance.application.commands.create_maintenance_date import CreateMaintenanceDateCommand
from maintenance.infraestructure.unit_of_work import UnitOfWork

class CreateMaintenanceDateHandler:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def handle(self, command: CreateMaintenanceDateCommand):
        entity = MaintenanceDate(
            id=0,  # o manejar ID autogenerado en base de datos
            date=command.date,
            hour=command.hour,
            maintenance_type=command.maintenance_type,
            staff=command.staff,
            customer_document_number=command.customer_document_number,
            customer_document_type=command.customer_document_type,
            store_id=command.store_id
        )

        with self.uow:
            self.uow.maintenance_date_repository.save(entity)
