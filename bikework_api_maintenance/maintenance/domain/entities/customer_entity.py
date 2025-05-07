from dataclasses import dataclass

@dataclass
class Customer:
    document_type: str
    document_number: str
    full_name: str
    address: str
    email: str
    phone_number: str