# application/interfaces/mediator.py

class Mediator:
    def __init__(self):
        self._handlers = {}

    def register(self, message_type, handler):
        self._handlers[message_type] = handler

    def send(self, message):
        handler = self._handlers.get(type(message))
        if handler is None:
            raise Exception(f"No handler registered for {type(message)}")
        return handler.handle(message)
