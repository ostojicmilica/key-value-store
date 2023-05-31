import unittest
from kvstore.kvstore import KeyValueStore

class TestKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.store = KeyValueStore()

    def test_put_and_get_value(self):
        self.store.put("key1", "value1")
        self.assertEqual(self.store.get("key1"), "value1")

    def test_put_and_delete_value(self):
        self.store.put("key1", "value1")
        self.store.delete("key1")
        self.assertIsNone(self.store.get("key1"))

    def test_get_nonexistent_value(self):
        self.assertIsNone(self.store.get("nonexistent_key"))

if __name__ == "__main__":
    unittest.main()
