# 🐳 **DOCKER BASICS**  

Welcome to **Docker Basics**! 🚀 In this project, I started by printing **"Hello, World!"** using Docker. This guide walks you through setting up a basic Dockerized Python application.  

---

## 📂 **Creating the Application File**  
First, create a Python file named **`app.py`** with a simple print statement:  

```python
print("Hello, World!")
```

---

## 📖 **Documentation & Resources**  
Here are some useful references for Docker:  
🔹 [Official Docker Documentation](https://docs.docker.com/)  
🔹 [Docker Desktop Guide](https://docs.docker.com/desktop/)  

---

## 🚀 **Deployment Guide**  

Follow these steps to deploy a basic application using Docker:  

### 🔹 **Step 1: Install Docker and Python**  
1️⃣ Download and install **Docker Desktop** → [Get it here](https://www.docker.com/products/docker-desktop/)  
2️⃣ Ensure Docker is running.  
3️⃣ Install **Docker** and **Python** extensions in your development environment.  

---

### 🔹 **Step 2: Verify Installation**  
Before proceeding, confirm that **Docker** and **Python** are installed:  

✅ Check Docker version:  
```bash
docker --version 
```  

✅ Check Python version:  
```bash
python --version 
```  

If both commands return valid versions, you’re good to go! 🎉  

---

### 🔹 **Step 3: Build & Run Your Dockerized Application**  

#### **🛠️ i) Build the Docker Image**  
Use the following command to build your Docker image:  
```bash
docker build -t myapp .
```  

#### **🔍 ii) Verify the Image Creation**  
Check if your Docker image was created successfully:  
```bash
docker images
```  

#### **▶️ iii) Run the Docker Container**  
Execute the container to print **"Hello, World!"** in the console:  
```bash
docker run myapp
```  

---

## 🎯 **Conclusion**  
This guide provides a structured approach to running your **first Dockerized Python application**. 🐳✨  

🔹 Next Steps: Explore Docker volumes, networking, and multi-container applications! 💡  

🚀 **Happy Docking!** ⚓🌊  

