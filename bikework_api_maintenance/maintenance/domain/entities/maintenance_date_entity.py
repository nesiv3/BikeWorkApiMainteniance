from dataclasses import dataclass
from datetime import date

@dataclass
class MaintenanceDate:
    id: int
    date: date
    hour: int
    maintenance_type: str
    staff: str
    customer_document_type: str
    customer_document_number: str
    store_id: int
