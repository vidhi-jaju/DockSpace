# 🐳 **Dockerized Streamlit Development Environment**  

This guide helps you set up a **Streamlit application** inside a **Docker container** for an efficient and portable development experience. 🚀  

---

## ✅ **Prerequisites**  
Before setting up the environment, ensure you have the following installed on your machine:  

🔹 **Docker** 🐳 (Ensure the Docker daemon is running)  
🔹 **Python 3.9+** 🐍 (Check installation with `python --version`)  
🔹 **pip** 📦 (Ensure it's up to date with `pip --version`)  
🔹 **Basic knowledge of Streamlit** 📊  

---

## 📂 **Directory Structure**  

```
project_root/
│── .streamlit/
│   └── config.toml
│── src/
│   └── main.py
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## 📜 **File Explanations**  

### **1️⃣ `.streamlit/config.toml`**  
This file configures Streamlit settings for local development.  

```toml
[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
```

---

### **2️⃣ `src/main.py`**  
This file contains the **core logic** of the Streamlit application, including:  

🏠 **Home Page** → Introduction to the app.  
📊 **Data Explorer** → Allows users to upload and inspect CSV files.  
📈 **Visualization Page** → Generates interactive charts and graphs.  

---

### **3️⃣ `Dockerfile`**  
Defines the containerized environment for Streamlit.  

```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim  

# Set working directory
WORKDIR /app  

# Copy dependencies and install them
COPY requirements.txt /app/  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy all project files
COPY . /app/  

# Expose Streamlit’s default port
EXPOSE 8501  

# Run the Streamlit app
CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

### **4️⃣ `requirements.txt`**  
Contains necessary dependencies:  

```text
streamlit
pandas
numpy
matplotlib
plotly
```

---

## ⚡ **Steps to Run the Project**  

### **1️⃣ Navigate to the project directory**  
```bash
cd path/to/project_root
```

### **2️⃣ Build the Docker image**  
```bash
docker build -t streamlit-app .
```

### **3️⃣ Run the container**  
```bash
docker run -p 8501:8501 streamlit-app
```

### **4️⃣ Open in Browser**  
🌐 Go to → [http://localhost:8501](http://localhost:8501)  

---

## 🎯 **Conclusion**  
You now have a **fully functional Streamlit environment** running inside Docker! 🚀  

![Streamlit App Screenshot](https://github.com/vidhi-jaju/DockSpace/blob/ffeee9124d5ab5508d44ce7cdb2debb5a6ce94b1/2.%20Dockerized%20Streamlit%20Development%20Environment/Images/Screenshot%202025-02-19%20013824.png?raw=true)
![Streamlit App Screenshot](https://github.com/vidhi-jaju/DockSpace/blob/ffeee9124d5ab5508d44ce7cdb2debb5a6ce94b1/2.%20Dockerized%20Streamlit%20Development%20Environment/Images/Screenshot%202025-02-19%20013835.png)
![Streamlit App Screenshot](https://github.com/vidhi-jaju/DockSpace/blob/ffeee9124d5ab5508d44ce7cdb2debb5a6ce94b1/2.%20Dockerized%20Streamlit%20Development%20Environment/Images/Screenshot%202025-02-19%20013853.png)


💡 **Next Steps:**  
🔹 Add more features to your Streamlit app.  
🔹 Deploy the containerized app on **AWS, GCP, or Azure**.  
🔹 Experiment with **Docker Compose** for multi-container applications.  

🚀 **Happy Coding!** 🐳💙
