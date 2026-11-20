"""
Observer Pattern
Define a one-to-many dependency so that when one object changes state,
all dependents are notified automatically.

Use cases: Event systems, pub/sub, UI updates.
"""
from abc import ABC, abstractmethod


class Event:
    def __init__(self, event_type: str, data=None):
        self.event_type = event_type
        self.data = data


class Observer(ABC):
    @abstractmethod
    def update(self, event: Event):
        pass


class EventEmitter:
    def __init__(self):
        self._observers = {}

    def subscribe(self, event_type: str, observer: Observer):
        if event_type not in self._observers:
            self._observers[event_type] = []
        self._observers[event_type].append(observer)

    def unsubscribe(self, event_type: str, observer: Observer):
        if event_type in self._observers:
            self._observers[event_type].remove(observer)

    def emit(self, event: Event):
        for observer in self._observers.get(event.event_type, []):
            observer.update(event)


class Logger(Observer):
    def update(self, event: Event):
        print(f"[LOG] {event.event_type}: {event.data}")


class EmailNotifier(Observer):
    def update(self, event: Event):
        print(f"[EMAIL] Sending notification about: {event.event_type}")


class MetricsCollector(Observer):
    def __init__(self):
        self.events_count = {}

    def update(self, event: Event):
        self.events_count[event.event_type] = self.events_count.get(event.event_type, 0) + 1
        print(f"[METRICS] {event.event_type} count: {self.events_count[event.event_type]}")


if __name__ == "__main__":
    emitter = EventEmitter()
    logger = Logger()
    notifier = EmailNotifier()
    metrics = MetricsCollector()

    emitter.subscribe("user_signup", logger)
    emitter.subscribe("user_signup", notifier)
    emitter.subscribe("user_signup", metrics)
    emitter.subscribe("purchase", logger)
    emitter.subscribe("purchase", metrics)

    emitter.emit(Event("user_signup", {"user": "alice"}))
    emitter.emit(Event("purchase", {"item": "book", "price": 29.99}))
    emitter.emit(Event("user_signup", {"user": "bob"}))
