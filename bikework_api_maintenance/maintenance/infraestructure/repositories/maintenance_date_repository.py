from maintenance.domain.entities.maintenance_date_entity import MaintenanceDate
from maintenance.infraestructure.models.maintenance_date_model import MaintenanceDate as MaintenanceDateModel

class MaintenanceDateRepository:
    def get_all(self):
        return [
            MaintenanceDate(
                id=m.id,
                date=m.date,
                hour=m.hour,
                maintenance_type=m.maintenance_type,
                staff=m.staff,
                customer_document_number=m.customer_document_number,
                customer_document_type=m.customer_document_type,
                store_id=m.store_id
            )
            for m in MaintenanceDateModel.objects.all()
        ]

    def get_by_id(self, maintenance_id: int):
        m = MaintenanceDateModel.objects.get(id=maintenance_id)
        return MaintenanceDate(
            id=m.id,
            date=m.date,
            hour=m.hour,
            maintenance_type=m.maintenance_type,
            staff=m.staff,
            customer_document_number=m.customer_document_number,
            customer_document_type=m.customer_document_type,
            store_id=m.store_id
        )

    def save(self, entity: MaintenanceDate):
        m = MaintenanceDateModel(
            id=entity.id,
            date=entity.date,
            hour=entity.hour,
            maintenance_type=entity.maintenance_type,
            staff=entity.staff,
            customer_document_number=entity.customer_document_number,
            customer_document_type=entity.customer_document_type,
            store_id=entity.store_id
        )
        m.save()
