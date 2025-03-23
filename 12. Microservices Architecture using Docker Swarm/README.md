# **🚀 Microservices Architecture with Docker Swarm ⚓**

## **Introduction**
This guide explains how to deploy a microservices architecture using **Docker Swarm**, featuring an **API Gateway** and a **Backend Service**.

---

## **Step 1: Install Docker & Initialize Docker Swarm**

### **1.1 Install Docker**
Ensure Docker is installed on your system. Verify with:

```bash
docker --version
```

If Docker is not installed, download and install it from the official site:  
🔗 [https://www.docker.com/get-started](https://www.docker.com/get-started)

👉 **Ensure that Docker Desktop is running in the background**.

### **1.2 Initialize Docker Swarm**
Start Docker Swarm by running:

```bash
docker swarm init
```

This command makes your machine the **Swarm Manager**.

---

## **Step 2: Project Setup**

### **📁 Project Structure**

```
microservices-docker-swarm/
│── backend-service/
│   ├── backend.py
│   ├── Dockerfile
│
│── api-gateway/
│   ├── api_gateway.py
│   ├── Dockerfile
│
│── docker-compose.yml
│── README.md
```

---

## **Step 3: Create the Microservices Code**

### **3.1 Backend Service**

#### **Create `backend.py`**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Vidhi Jaju"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

#### **Create `Dockerfile` for Backend**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY backend.py /app
RUN pip install flask
CMD ["python", "backend.py"]
```

---

### **3.2 API Gateway Service**

#### **Create `api_gateway.py`**
```python
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    backend_response = requests.get('http://backend-service:5000')
    return f"API Gateway: {backend_response.text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

#### **Create `Dockerfile` for API Gateway**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY api_gateway.py /app
RUN pip install flask requests
CMD ["python", "api_gateway.py"]
```

---

## **Step 4: Build Docker Images**
Navigate to your project directory and build the images:

```bash
docker build -t backend-service ./backend-service
docker build -t api-gateway ./api-gateway
```

Verify the built images:

```bash
docker images
```

---

## **Step 5: Create Docker Compose File for Swarm**

Create `docker-compose.yml` in the root directory:

```yaml
version: '3.7'

services:
  backend-service:
    image: backend-service
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    networks:
      - app-network
    ports:
      - "5000:5000"

  api-gateway:
    image: api-gateway
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    networks:
      - app-network
    ports:
      - "8080:8080"
    depends_on:
      - backend-service

networks:
  app-network:
    driver: overlay
```

---

## **Step 6: Deploy the Microservices to Docker Swarm**

Deploy your services to the **Docker Swarm cluster** using:

```bash
docker stack deploy -c docker-compose.yml my_microservices
```

---

## **Step 7: Verify the Deployment**

Check the running services:

```bash
docker stack services my_microservices
```

List the running containers:

```bash
docker ps
```

---

## **Step 8: Access the Microservices**

Open a browser and go to:

```
http://localhost:8080
```

Expected output:
```
API Gateway: Vidhi Jaju
```

---

## **Step 9: Scaling the Services**

Increase the number of backend service replicas to **5**:

```bash
docker service scale my_microservices_backend-service=5
```

Verify the scaled services:

```bash
docker stack services my_microservices
```

---

## **Step 10: Updating the Services**

If you make changes to `backend.py`, rebuild the image:

```bash
docker build -t backend-service ./backend-service
```

Then update the service in Swarm:

```bash
docker service update --image backend-service:latest my_microservices_backend-service
```

---

## **Step 11: Removing the Stack & Leaving Swarm**

To **remove the deployed stack**, run:

```bash
docker stack rm my_microservices
```

To **leave Docker Swarm**, run:

```bash
docker swarm leave --force
```

---

## **🎉 Conclusion**

You have successfully deployed a **microservices architecture** using **Docker Swarm** with an API Gateway and a Backend Service. 🚀

