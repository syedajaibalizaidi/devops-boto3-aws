# Multi-Cloud Automation Toolkit ☁️

Collection of Boto3(Pyhton) scripts for managing AWS and Linode cloud resources with focus on:  
**EC2 maintenance • EKS clusters • Monitoring • Backup solutions**

## 📂 Scripts Overview

| Script | Description | Cloud | Dependencies |
|--------|-------------|-------|--------------|
| [add-env-tags.py](/add-env-tags.py) | Adds environment tags (prod/dev) to resources | AWS + Linode | boto3, python-linode-api |
| [cleaup-snapshot.py](/cleaup-snapshot.py) | Automated cleanup of old snapshots | AWS (EC2 EBS) | boto3 |
| [ec2-data-backup.py](/ec2-data-backup.py) | Creates timestamped EC2 backups | AWS | boto3 |
| [ec2-health-check.py](/ec2-health-check.py) | Checks EC2 instance health status | AWS | boto3 |
| [eks-cluster.py](/eks-cluster.py) | EKS cluster lifecycle management | AWS | eksctl, boto3 |
| [restore-ec2-data.py](/restore-ec2-data.py) | Restores EC2 from backup snapshots | AWS | boto3 |
| [schedule-task.py](/schedule-task.py) | Schedules cloud tasks via Lambda/CRON | AWS + Linode | boto3, python-linode-api |
| [web-monitoring.py](/web-monitoring.py) | Website uptime monitoring with alerts | Multi-cloud | requests, slack-sdk |
