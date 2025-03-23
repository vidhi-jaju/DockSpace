# Bakery Foundation Example on Windows 🍞

## Overview
This guide provides step-by-step instructions on setting up and using Packer to create a machine image (AMI) on AWS. It covers installation, configuration, and deployment on Windows.

## Prerequisites
Before starting, ensure you have:
- A Windows machine with administrator access.
- An AWS account with IAM credentials.
- Basic knowledge of AWS and PowerShell.

## Step 1: Install Required Tools

### 1.1 Install Packer
#### Step 1: Download Packer
- Open your browser and go to the [Packer Download Page](https://developer.hashicorp.com/packer/downloads).
- Download the latest Windows (64-bit) ZIP file.

#### Step 2: Extract Packer
- Navigate to the downloaded ZIP file.
- Right-click and select **Extract All...**
- Move `packer.exe` to `C:\packer` (Create this folder if it doesn’t exist).

#### Step 3: Add Packer to System PATH
- Open **Environment Variables** (Search for it in Windows).
- Click **Environment Variables** → Under **System Variables**, find **Path** → Click **Edit**.
- Click **New**, then add:
  ```
  C:\packer
  ```
- Click **OK** and close all windows.

#### Step 4: Verify Packer Installation
Open PowerShell and run:
```powershell
packer --version
```
✅ If successful, the Packer version will be displayed.

### 1.2 Install AWS CLI
#### Step 1: Download AWS CLI
- Go to the [AWS CLI Download Page](https://aws.amazon.com/cli/).
- Download and run the `AWSCLI.msi` installer.

#### Step 2: Install AWS CLI
- Follow the on-screen steps: **Next** → **Next** → **Finish**.
- Verify installation:
  ```powershell
  aws --version
  ```
  ✅ If successful, it should display something like: `aws-cli/2.x.x Windows/10`

### 1.3 Configure AWS CLI (5 minutes)
Run the following command in PowerShell:
```powershell
aws configure
```
Enter the following when prompted:
- **AWS Access Key ID:** `<Your AWS Key>`
- **AWS Secret Access Key:** `<Your AWS Secret>`
- **Default region name:** `us-east-1` (or your preferred region)
- **Default output format:** `json` (Press Enter)
✅ AWS CLI is now configured.

## Step 2: Create the Packer Template

### 2.1 Create the Packer HCL File
1. Open **Notepad** or **VS Code**.
2. Copy the following code into a new file:
```hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.0.0"
    }
  }
}

variable "aws_region" {
  default = "us-east-1"
}

source "amazon-ebs" "python39" {
  ami_name      = "bakery-foundation-python39-${formatdate("YYYYMMDD-HHmmss", timestamp())}"
  instance_type = "t2.micro"
  region        = var.aws_region
  source_ami    = "ami-0a25f237e97fa2b5e"
  ssh_username  = "ubuntu"
}

build {
  sources = ["source.amazon-ebs.python39"]

  provisioner "shell" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y python3.9 python3.9-venv python3.9-dev"
    ]
  }
}
```
3. Save the file as `bakery.pkr.hcl` in `C:\packer`.

### 2.2 Find a Valid Ubuntu AMI
Run the following AWS CLI command to get the latest Ubuntu AMI:
```powershell
aws ec2 describe-images --owners 099720109477 --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*" --query "Images | sort_by(@, &CreationDate)[-1].ImageId" --output text
```
✅ Update `bakery.pkr.hcl` by replacing the `source_ami` with the new AMI ID:
```hcl
source "amazon-ebs" "python39" {
  source_ami = "ami-xxxxxxxxxxxxxxx"  # Replace with actual AMI ID
}
```

## Step 3: Validate and Build the Image

### 3.1 Initialize and Validate Packer Template
Open PowerShell and navigate to `C:\packer`:
```powershell
cd C:\packer
```
Initialize Packer:
```powershell
packer init .
```
Validate the template:
```powershell
packer validate bakery.pkr.hcl
```
✅ Expected Output: `The configuration is valid.`

### 3.2 Build the Machine Image
Run the following command:
```powershell
packer build bakery.pkr.hcl
```
This will:
- Create a temporary EC2 instance.
- Install Python 3.9.
- Convert it into an Amazon Machine Image (AMI).
- Delete the temporary instance.

## Step 4: Deploy and Test the AMI

### 4.1 Find the AMI
1. Log in to [AWS Console](https://aws.amazon.com/console/).
2. Navigate to **EC2 → AMIs** (Set the region you used when creating the AMI).
3. Find the AMI named: `bakery-foundation-python39-timestamp`

### 4.2 Launch an EC2 Instance with Your AMI
1. Go to **AWS EC2 Console**: [AWS EC2 Dashboard](https://console.aws.amazon.com/ec2/).
2. Click **Launch Instance** → **My AMIs** (Left Sidebar).
3. Search for your AMI and **Select It**.
4. Choose:
   - **Instance Type:** `t2.micro` (or higher, based on your needs).
   - **Key Pair:** Use an existing key or create a new one.
   - **Security Group:** Allow **SSH (port 22)** and other required ports.
5. Click **Launch! 🚀**

### 4.3 Connect to the Instance
1. Get the Public IP from the EC2 Console.
2. Open PowerShell and connect via SSH:
   ```powershell
   ssh -i "C:\path\to\your-key.pem" ubuntu@your-instance-ip
   ```
3. Accept the SSH key fingerprint (First Time Only): Type `yes` and press Enter.
✅ You are now logged into your EC2 instance! 🎉

### 4.4 Verify Python Installation
Once inside the instance, run:
```bash
python3.9 --version
```
✅ Expected Output: `Python 3.9.5`

## Conclusion
You have successfully set up Packer, created an AWS AMI, and deployed an EC2 instance with Python 3.9! 🚀

---



