# application/commands/create_maintenance_date.py

from dataclasses import dataclass
from datetime import date

@dataclass
class CreateMaintenanceDateCommand:
    date: date
    hour: int
    maintenance_type: str
    staff: str
    customer_document_number: str
    customer_document_type: str
    store_id: int
