#!/bin/bash

sudo yum update -y
sudo yum install -y fail2ban git amazon-cloudwatch-agent

sudo systemctl enable fail2ban
sudo systemctl start fail2ban

echo "System hardened and CloudWatch ready."
