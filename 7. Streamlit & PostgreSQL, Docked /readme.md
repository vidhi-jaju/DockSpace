# Deploying a Streamlit App with PostgreSQL in Docker

## 📌 Overview
This project demonstrates how to deploy a **Streamlit application** that connects to a **PostgreSQL database** using **Docker**. The application fetches and displays passenger data stored in PostgreSQL, ensuring a seamless and containerized workflow.

---

## 💁 Project Structure
```
Streamlit-Postgres-Docker/
│── Dockerfile
│── main.py
```

### 🔹 Description of Files:
- **main.py** – Streamlit app that connects to PostgreSQL and fetches data.
- **Dockerfile** – Configuration for containerizing the Streamlit app.

---

## 🛠 Setting Up PostgreSQL in Docker
### Step 1: Pull the PostgreSQL Docker Image
```sh
docker pull postgres
```

### Step 2: Create a Docker Network
```sh
docker network create my_postgres_network
```
This network allows PostgreSQL and the Streamlit app to communicate.

### Step 3: Run the PostgreSQL Container
```sh
docker run --name my_postgres_container --network my_postgres_network -e POSTGRES_USER=vidhi -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=testdb -p 5432:5432 -d postgres
```
This starts a PostgreSQL container with authentication settings.

---

## 💊 Creating and Populating the Database
### Step 4: Access PostgreSQL
```sh
docker exec -it my_postgres_container psql -U vidhi -d testdb
```

### Step 5: Create the `passengers` Table
```sql
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);
```

### Step 6: Insert Sample Data
```sql
INSERT INTO passengers (name, location) VALUES
('Vidhi', 'Pathankot'),
('Aryan', 'Jind'),
('Coach Saab', 'Atta');
```

---

## 🎨 Streamlit Application (`main.py`)
This script connects to PostgreSQL, fetches data, and displays it in a Streamlit UI with enhanced styling.

### 🔹 Key Features:
- Connects to PostgreSQL using **psycopg2**.
- Retrieves and displays passenger data dynamically.
- Uses **CSS styling** to improve the UI.

---

## 🐛 Dockerizing the Streamlit Application
### Step 7: Create a `Dockerfile`
```dockerfile
FROM python:3.9
WORKDIR /app
COPY main.py .
RUN pip install streamlit psycopg2
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🚀 Running the Streamlit Application in Docker
### Step 8: Build the Docker Image
```sh
docker build -t streamlit_app .
```

### Step 9: Run the Streamlit Container
```sh
docker run --name my_streamlit_container --network my_postgres_network -p 8501:8501 -d streamlit_app
```
This ensures that the Streamlit app can communicate with PostgreSQL.

---

## 🔗 Access the Application
Open a browser and navigate to:
👉 **[http://localhost:8501](http://localhost:8501)**

You should see the list of passengers displayed in the app.

---

## 🎯 Summary
✅ PostgreSQL container stores passenger data.  
✅ Streamlit container fetches and displays data from PostgreSQL.  
✅ Both containers communicate over **my_postgres_network**.  
✅ Application accessible at **http://localhost:8501**.  

This project provides a **containerized solution** for data visualization using **Streamlit and PostgreSQL**. 🚀

