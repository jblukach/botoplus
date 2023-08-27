# botoplus

Cloud Security Posture Management (CSPM) is a crowded market space with all the commercial and open-source offerings. Why do we need yet another set of Python Boto3 scripts? 

Having written so much code over the years, it was time for a more extensible framework addressing common pitfalls while maintaining flexibility for AWS Security Operations. 

**Common Pitfalls**

- [x] Identity Access Management (SSO)
- [x] User Interface (Jupyter Notebooks)

### Getting Started

| Notebook | Description |
| -------- | ----------- |
| [Authentication](authentication.ipynb) | GitHub Codespaces: AWS CLIv2 and Python Library Configuration |

### Cloud Development Kit (CDK)

| Notebook | Description |
| -------- | ----------- |
| [Identify CDK Bootstraps](cdk/identify-cdk-bootstraps.ipynb) | Identify CDK Bootstraps with Versions for All Accounts & Regions |

### Elastic Compute Cloud (EC2)

| Notebook | Description |
| -------- | ----------- |
| [Public Amazon Machine Images](ec2/public-amazon-machine-images.ipynb) | Find Public Amazon Machine Images |

### Organizations

| Notebook | Description |
| -------- | ----------- |
| [Identify Privileged Accounts](organizations/identify-privileged-accounts.ipynb) | List of Delegated Administration Accounts & Services |

### Security Hub

| Notebook | Description |
| -------- | ----------- |
| [Minimal Cost Configuration](securityhub/minimal-cost-configuration.ipynb) | Disable All Standards & Limit Subscriptions (IAM Analyzer & Health) |

### Simple Storage Service (S3)

| Notebook | Description |
| -------- | ----------- |
| [Public CORS Configuration](s3/public-cors-configuration.ipynb) | Find potentially public S3 Buckets with CORS Configured |

### Virtual Private Cloud (VPC)

| Notebook | Description |
| -------- | ----------- |
| [IP Address Conflicts](vpc/ip-address-conflicts.ipynb) | Identify IP address conflicts, default VPCs, & IPv6 configs |
