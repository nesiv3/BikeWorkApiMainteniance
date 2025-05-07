# application/handlers/get_all_maintenance_dates_handler.py

from maintenance.application.queries.get_all_maintenance_dates import GetAllMaintenanceDatesQuery

class GetAllMaintenanceDatesHandler:
    def __init__(self, uow):
        self.uow = uow

    def handle(self, query: GetAllMaintenanceDatesQuery):
        with self.uow:
            return self.uow.maintenance_date_repository.get_all()
