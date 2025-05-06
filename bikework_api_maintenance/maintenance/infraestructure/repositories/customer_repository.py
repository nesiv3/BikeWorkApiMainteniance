from maintenance.domain.models import Customer as CustomerDomain
from maintenance.infraestructure.orm.models import Customer as CustomerORM

class CustomerRepository:
    def get_all(self):
        return [CustomerDomain(id=c.id, full_name=c.full_name, address=c.address,phone_number=c.phone_number,email=c.email) for c in CustomerORM.objects.all()]

    def add(self, customer_dto):
        customer = CustomerORM.objects.create(
            full_name=customer_dto.full_name,
            address=customer_dto.address
        )
        return CustomerDomain(id=customer.id, full_name=customer.full_name, address=customer.address,phone_number=customer.phone_number,email=customer.email)