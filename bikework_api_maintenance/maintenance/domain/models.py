from dataclasses import dataclass

@dataclass
class Customer:
    id: int
    full_name: str
    address: str
    phone_number: str
    email: str
    