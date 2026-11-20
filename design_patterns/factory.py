"""
Factory Pattern
Create objects without specifying exact classes.

Use cases: Database connectors, file parsers, UI components.
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str):
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass


class EmailNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"Sending EMAIL to {recipient}: {message}")

    def get_type(self) -> str:
        return "email"


class SMSNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"Sending SMS to {recipient}: {message}")

    def get_type(self) -> str:
        return "sms"


class PushNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"Sending PUSH to {recipient}: {message}")

    def get_type(self) -> str:
        return "push"


class SlackNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"Sending SLACK to #{recipient}: {message}")

    def get_type(self) -> str:
        return "slack"


class NotificationFactory:
    _creators = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification,
        "slack": SlackNotification,
    }

    @classmethod
    def create(cls, notification_type: str) -> Notification:
        creator = cls._creators.get(notification_type)
        if not creator:
            raise ValueError(f"Unknown notification type: {notification_type}")
        return creator()

    @classmethod
    def register(cls, notification_type: str, creator):
        cls._creators[notification_type] = creator


if __name__ == "__main__":
    for ntype in ["email", "sms", "push", "slack"]:
        notification = NotificationFactory.create(ntype)
        notification.send("Hello World!", "user@example.com")
