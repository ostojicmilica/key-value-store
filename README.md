# Key-Value Store Implementation

## Technology Overview

- Programming Language: Python
- Web Framework: Flask
- Containerization: Docker
- Orchestration: Kubernetes

**Reasoning behind choosing these technologies:**

- Python: Chosen for its simplicity. Python allows rapid development and is well-suited for building web applications.
- Flask: A lightweight and flexible web framework that enables the creation of RESTful APIs. 
- Docker: Used for containerizing the application, providing consistency across environments and facilitating deployment.
- Kubernetes: Enables scalable and resilient deployment of the key-value store by managing containerized instances.

## Design of Data Structures

- Key-Value Store: Implemented using a dictionary (hash map) data structure in Python. This data structure allows efficient key-based lookups, insertions, and deletions.

## Performance Characteristics

- **Concurrency**: The key-value store supports simultaneous access by multiple clients using multi-threading and synchronization mechanisms. This enables concurrent handling of requests and improves scalability.
- **In-Memory Storage**: The key-value store stores data only in memory, resulting in fast read and write operations. However, data is not persisted, and restarting the application will cause data loss.
- **Thread Safety**: The implementation ensures thread safety by utilizing locks to synchronize access to the shared data structure, preventing data corruption or race conditions.

## Assumptions

- **Horizontal Scaling**: The key-value store can be horizontally scaled by running multiple instances on Kubernetes. However, dynamic scaling is not implemented in this version, and the number of instances must be specified on startup.
- **Network Interface**: The implementation uses a simple RESTful API for the network interface
- **Variable-Length Keys and Values**: The key-value store supports strings as both keys and values. The length of the keys and values can vary according to the application's needs.

---