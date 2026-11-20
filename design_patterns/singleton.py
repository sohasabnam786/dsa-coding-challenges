"""
Singleton Pattern
Ensure a class has only one instance and provide a global point of access.

Use cases: Configuration, logging, connection pools.
"""


class SingletonMeta(type):
    """Thread-safe Singleton metaclass."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self, connection_string: str = ""):
        self.connection_string = connection_string
        self._connected = False

    def connect(self):
        self._connected = True
        print(f"Connected to {self.connection_string}")

    def query(self, sql: str):
        if not self._connected:
            self.connect()
        print(f"Executing: {sql}")
        return f"Results for: {sql}"


class SingletonDecorator:
    """Alternative: Singleton as decorator."""
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance


if __name__ == "__main__":
    db1 = Database("postgresql://localhost/mydb")
    db2 = Database("mysql://localhost/other")

    print(f"Same instance? {db1 is db2}")  # True
    print(f"Connection: {db1.connection_string}")  # postgresql://localhost/mydb
