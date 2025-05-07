class UnitOfWork:
    def __init__(self, maintenance_date_repository):
        self.maintenance_date_repository = maintenance_date_repository

    def __enter__(self):
        # Aquí podrías manejar transacciones si se necesita
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Finalizar la transacción
        if exc_type:
            # rollback
            pass
        else:
            # commit
            pass