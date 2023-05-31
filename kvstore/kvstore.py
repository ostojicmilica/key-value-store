import threading

class KeyValueStore:
    def __init__(self):
        self.store = {}

    def put(self, key, value):
        with threading.Lock():
            self.store[key] = value

    def get(self, key):
        return self.store.get(key)

    def delete(self, key):
        with threading.Lock():
            if key in self.store:
                del self.store[key]