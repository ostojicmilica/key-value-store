import threading

class KeyValueStore:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def put(self, key, value):
        with self.lock:
            if not isinstance(key, str) or not isinstance(value, str):
                raise ValueError("Key and value must be strings")
            self.data[key] = value

    def get(self, key):
        with self.lock:
            if not isinstance(key, str):
                raise ValueError("Key must be a string")
            return self.data.get(key)

    def delete(self, key):
        with self.lock:
            if not isinstance(key, str):
                raise ValueError("Key must be a string")
            if key in self.data:
                del self.data[key]
                return True
            else:
                return False