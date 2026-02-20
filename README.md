🚀 AWS Cloud Security Project – Final Year Project
Secure Multi-Tier AWS Architecture & Shadow Identity Detection System
<div align="center">

🛡️ Cloud Security • ☁️ AWS Architecture • 👤 Identity Governance • 🔍 Shadow Account Detection

</div>
📌 📚 Project Overview

This project implements a production-grade secure AWS environment focusing on:

Zero-Trust Identity Architecture

VPC Network Segmentation

IAM Hardening

Shadow Identity Detection

EC2 Instance Hardening

S3 & CloudTrail Monitoring

Automated Auditing Scripts

Goal: Build a security-focused cloud infrastructure following AWS Well-Architected & industry best practices.

🧱 🔒 1. Secure VPC Architecture
aws-configurations/VPC/

Contains:

Custom VPC (10.0.0.0/16)

Public & Private Subnets

NAT Gateway

Internet Gateway

Route Tables

Network Isolation Design

👥 🔑 2. Identity & Access Management (IAM)
aws-configurations/IAM-Users/
aws-configurations/IAM-Roles/
aws-configurations/Policies/

Includes:

Admin User (Scoped Admin Policy)

Restricted User

Audit Role

S3 Restricted Policy

MFA Enforced

Access Key Governance

Least Privilege Architecture

💻 🛠️ 3. EC2 Instance Hardening
aws-configurations/EC2/
scripts/ec2-hardening.sh

Hardening Measures:

Amazon Linux 2023

gp3 EBS Encryption

Fail2Ban

SSH Key Authentication

CloudWatch Logs Integration

OS-Level Security Enhancements

📡 📊 4. Monitoring & Logging
aws-configurations/CloudTrail/
aws-configurations/CloudWatch/

Monitoring Setup:

CloudTrail (ALL regions)

CloudWatch Alerts

Unauthorized API alarm

Root login alarm

IAM misuse alerts

JSON log formatting

👤 🕵️‍♂️ 5. Shadow Identity Detection System
scripts/shadow-identity-detection.py

Detects:

Unused IAM Users

Unused Access Keys

Stale Roles

No-MFA Users

Suspicious Accounts
