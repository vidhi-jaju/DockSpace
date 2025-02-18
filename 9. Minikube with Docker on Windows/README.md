# Minikube with Docker on Windows ☸️

<p align="center">
  <img src="https://raw.githubusercontent.com/TarakKatoch/My-Docker-Dockyard/54505203108590859cc273cd9a1c18bb9f018e76/Minikube%20with%20Docker%20on%20Windows/assets/logo.png" alt="Minikube Logo" width="200" />
</p>

## What is Minikube? 

**Minikube** is a tool that helps you run a local Kubernetes cluster on your machine. It's perfect for developers who want to experiment with Kubernetes without setting up a large cloud infrastructure. Minikube provides a simple way to start a Kubernetes cluster on a local machine, and it works with various drivers like Docker, VirtualBox, and Hyper-V.

Minikube makes Kubernetes accessible for local development, testing, and experimentation. It simplifies the process of deploying and managing Kubernetes clusters locally without the need for extensive resources.

---

## What is Kubernetes? ☸️

**Kubernetes** is an open-source platform for automating the deployment, scaling, and management of containerized applications. It orchestrates and manages containers (such as those created with Docker) to ensure that applications run reliably and efficiently, whether in a development, test, or production environment.

Kubernetes allows you to:
- Deploy applications in containers across clusters.
- Scale applications up or down with ease.
- Manage containerized workloads with minimal effort.
- Ensure high availability, load balancing, and fault tolerance for your applications.

By using Kubernetes, developers can focus on writing code and let Kubernetes manage the complexity of application deployment and scaling.

---

## ✅ Step 1: Install Required Tools

Before starting, ensure you have the necessary software installed.

### 1. Install Docker Desktop 🐋

Minikube can run Kubernetes inside a Docker container, so install Docker Desktop:

- [Download and install Docker Desktop](https://www.docker.com/products/docker-desktop/)

**During installation:**
- Make sure WSL 2 backend is enabled (recommended). ⚙️
- If you have Windows Pro/Enterprise, enable Hyper-V (Docker will handle this). 🔧

### 2. Install Minikube 📦

To download and install Minikube, open CMD or PowerShell as Administrator and run the following command:
```bash
choco install minikube
```
If you don't have Chocolatey, [install Minikube manually](https://minikube.sigs.k8s.io/docs/start/).

### 3. Install kubectl

```bash
choco install kubernetes-cli
```
Verify installation:
```bash
kubectl version --client
```
![image](https://github.com/vidhi-jaju/DockSpace/blob/e8159bccb2036cd49d457e38687b868940b3800f/9.%20Minikube%20with%20Docker%20on%20Windows/images/1.png)
![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/2.png)
![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/3.png)
![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/4.png)

![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/5.png)

![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/6.png)

---

## ✅ Step 2: Start Minikube with Docker Driver 🐳

Now, start Minikube using Docker as the driver. Ensure that your Docker Engine (Docker Desktop) is running in the background.

### 1. Start Minikube
```bash
minikube start --driver=docker
```
This initializes a Kubernetes cluster inside a Docker container instead of a virtual machine.

Check the status:
```bash
minikube status
```
![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/7.png)

---

## ✅ Step 3: Deploy an Application 🚀

Deploy a simple application (nginx).

### 1. Create an Nginx Deployment
```bash
kubectl create deployment nginx --image=nginx
```

### 2. Expose the Deployment 🔓
```bash
kubectl expose deployment nginx --type=NodePort --port=80
```

### 3. Get the Service URL 🔗
```bash
minikube service nginx --url
```
Open the URL in your browser to see the running nginx web server. 🌐

![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/8.png)

---

## ✅ Step 4: Manage Kubernetes Cluster

### 1. Check Running Pods 📋
```bash
kubectl get pods
```

### 2. Scale the Deployment 📏
Scale to 3 replicas:
```bash
kubectl scale deployment nginx --replicas=3
```
Check pods again:
```bash
kubectl get pods
```

### 3. Delete the Deployment 🧹
```bash
kubectl delete service nginx
kubectl delete deployment nginx
```
![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/9.png)

---

## ✅ Step 5: Stop and Delete Minikube 🗑️

### 1. Stop Minikube
```bash
minikube stop
```

### 2. Delete the Cluster 
```bash
minikube delete
```
This removes all Kubernetes resources.
![image](https://github.com/vidhi-jaju/DockSpace/blob/54b356d888b5072f9cd4f80b69f6c1bf9277a7df/9.%20Minikube%20with%20Docker%20on%20Windows/images/10.png)

---

## 🎯 Conclusion

By using Minikube with Docker, you can run Kubernetes locally without needing Hyper-V or VirtualBox. Docker provides an easy way to manage your cluster and experiment with Kubernetes.

🚀😊


