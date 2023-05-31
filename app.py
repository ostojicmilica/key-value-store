from flask import Flask, jsonify, request
from kvstore.kvstore import KeyValueStore
import threading

app = Flask(__name__)
store = KeyValueStore()

@app.route('/key', methods=['PUT'])
def put():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    store.put(key, value)
    return jsonify({'message': 'Key added/updated successfully'})

@app.route('/key/<key>', methods=['GET'])
def get(key):
    value = store.get(key)
    if value is None:
        return jsonify({'message': 'Key not found'}), 404
    return jsonify({'key': key, 'value': value})

@app.route('/key/<key>', methods=['DELETE'])
def delete(key):
    success = store.delete(key)
    if not success:
        return jsonify({'message': 'Key not found'}), 404
    return jsonify({'message': 'Key deleted successfully'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)