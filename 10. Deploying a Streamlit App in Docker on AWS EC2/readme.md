# 🚀 Deploying a Streamlit App in Docker on AWS EC2

## 📌 Overview
This guide provides a step-by-step approach to deploying a Streamlit app inside a Docker container on an AWS EC2 instance with a custom network setup. It covers:

✅ Setting up a VPC, Subnet, Route Table, and Internet Gateway  
✅ Launching and configuring an EC2 instance  
✅ Installing and configuring Docker  
✅ Transferring project files to EC2  
✅ Running the Streamlit app inside a Docker container  
✅ Managing the Docker container  

---

## 📖 Table of Contents-
1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway  
2️⃣ Launching and Configuring an EC2 Instance  
3️⃣ Connecting to EC2  
4️⃣ Setting Permissions for the PEM Key  
5️⃣ Installing and Configuring Docker  
6️⃣ Copying Project Files to EC2  
7️⃣ Building and Running the Docker Container  
8️⃣ Accessing the Streamlit App  
9️⃣ Managing the Docker Container  

---

## 1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway

### 🔹 Create a New VPC
Go to AWS Console → VPC Dashboard → Create VPC  
- **Name:** MyCustomVPC  
- **IPv4 CIDR block:** 10.0.0.0/16  

![img1](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/1.png)

### 🔹 Create a Subnet
Go to VPC Dashboard → Subnets → Create Subnet  
- **Select:** MyCustomVPC  
- **Subnet name:** MyPublicSubnet  
- **CIDR block:** 10.0.1.0/24  
- **Enable Auto-assign Public IPv4**  

![img2](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/2.png)

### 🔹 Create an Internet Gateway and Attach to VPC
- **Name:** MyIGW  
- **Attach it to:** MyCustomVPC  

![img3](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/3.png)

### 🔹 Create and Associate a Route Table
- **Name:** MyPublicRouteTable  
- **Destination:** 0.0.0.0/0  
- **Target:** MyIGW  
- **Associate with:** MyPublicSubnet  

![img4](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/4.png)

---

## 2️⃣ Launching and Configuring an EC2 Instance

### 🔹 Launch an EC2 Instance
- **Name:** Streamlit-EC2  
- **AMI:** Amazon Linux 2023  
- **Instance Type:** t2.micro (Free Tier)  
- **Key Pair:** Select/Create a key pair  
- **Network:** MyCustomVPC  
- **Subnet:** MyPublicSubnet  
- **Enable Auto-assign Public IP**  
- **Security Group:** Allow SSH (22), HTTP (80), Streamlit (8501)  

![img5](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/5.png)

---

## 3️⃣ Connecting to EC2

### 🔹 Via EC2 Instance Connect
Go to EC2 Dashboard → Select Instance → Click Connect  
- **Choose:** EC2 Instance Connect  
- **Click:** Connect  

![img6](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/6.png)

---

## 4️⃣ Setting Permissions for the PEM Key
```sh
mv /path/to/your-key.pem ~/your-work-directory/
chmod 600 your-key.pem
```

---

## 5️⃣ Installing and Configuring Docker
```sh
sudo yum update -y
sudo yum install -y docker
sudo systemctl enable docker
sudo systemctl start docker
```

![img7](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/7.png)

---

## 6️⃣ Copying Project Files to EC2
```sh
scp -i your-key.pem app.py Dockerfile requirements.txt mushrooms.csv ec2-user@your-ec2-public-ip:/home/ec2-user/
```

![img8](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/8.png)

---

## 7️⃣ Building and Running the Docker Container

### 🔹 Connect to EC2 and navigate to project directory
```sh
cd /home/ec2-user
```
### 🔹 Build the Docker image
```sh
sudo docker build -t streamlit-app .
```

![img9](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/9.png)

### 🔹 Run the container
```sh
sudo docker run -d -p 8501:8501 --name streamlit_container streamlit-app
```

![img10](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/10.png)

---

## 8️⃣ Accessing the Streamlit App
🌐 Open your browser and visit:
```sh
http://your-ec2-public-ip:8501
```

![img11](https://github.com/vidhi-jaju/DockSpace/blob/84980abb1c4a643320f44cdf69efd0a0547dec32/10.%20Deploying%20a%20Streamlit%20App%20in%20Docker%20on%20AWS%20EC2/Images/11.png)


9️⃣ Managing the Docker Container

🔹 Check running containers
```sh
sudo docker ps
```
🔹 Stop the container
```sh
sudo docker stop streamlit_container
```
🔹 Remove the container
```sh
sudo docker rm streamlit_container
```
🔹 Restart the container
```sh
sudo docker start streamlit_container
```
---
## 🎯 Conclusion
This guide helps you deploy a Streamlit app inside a Docker container on AWS EC2 with a custom VPC setup. The deployment ensures scalability, security, and high availability for your application. 🚀🎉

✅ Happy Deploying! 🖥️🐳☁️

