AWS Cloud Security Project – Final Year Project
Secure Multi-Tier AWS Architecture with Shadow Identity Detection

This repository contains the complete implementation, documentation, and automation code for building a secure AWS environment, detecting shadow identities, and enforcing IAM governance.

🔒 Project Objective

Build a secure, production-grade AWS environment with:

Custom VPC Design

Public + Private Subnet Architecture

IAM Hardening & Role-Based Access Control

EC2 Hardening & EBS Encryption

CloudTrail + CloudWatch Monitoring

Shadow Identity Detection Script

S3 Permission Restriction Policies

Real-World Security Best Practices

🧩 Project Components
1️⃣ Secure VPC Architecture

Custom VPC (10.0.0.0/16)

Public Subnet for NAT Gateway

Private Subnet for EC2

Internet Gateway (IGW)

Route Tables + Associations

📁 Folder: aws-configurations/VPC/

2️⃣ IAM Architecture

Admin User with custom policy

Restricted User (Least privilege)

Audit Role

S3 Restricted Read Policy

MFA Enforcement

📁 Folder: aws-configurations/IAM-Users/
📁 Folder: aws-configurations/Policies/

3️⃣ EC2 Instance Hardening

Amazon Linux 2023

Security Group (SSH + HTTP only)

EBS Volume with Encryption

CloudWatch Agent installation

Log streaming

📁 Folder: aws-configurations/EC2/
📁 Folder: scripts/ec2-hardening.sh

4️⃣ Monitoring & Logging

CloudTrail enabled

CloudWatch Alarms

Unauthorised API call alerts

Root login alerts

📁 Folder: aws-configurations/CloudTrail/
📁 Folder: aws-configurations/CloudWatch/

5️⃣ Shadow Identity Detection

A Python script that:

Detects IAM users not used for 90+ days

Detects unused access keys

Detects stale IAM roles

Alerts using CloudWatch

📁 Folder: scripts/shadow-identity-detection.py

6️⃣ Documentation

Stage 1, 2, 3 Reports

IEEE Research Paper

Final Presentation

📁 Folder: documentation/

🏗️ Project Architecture Diagram

Place your main diagram here:

📁 Folder: architecture-diagrams/architecture.png
