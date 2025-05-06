from maintenance.application.dtos.customer_dto import CustomerDTO

class CreateCustomerCommand:
    def __init__(self, customer_dto):
        self.customer_dto = customer_dto

class CreateCustomerHandler:
    def __init__(self, repository):
        self.repository = repository

    def handle(self, command: CreateCustomerCommand):
        if not isinstance(command, CreateCustomerCommand):
            raise TypeError("Expected command to be an instance of CreateCustomerCommand")
        return self.repository.add(command.customer_dto)
