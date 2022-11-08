# botoplus

Cloud Security Posture Management (CSPM) is a crowded market space with all the Open-Source and Vendor offerings. Why do we need yet another set of Python Boto3 scripts?

Having written so much code over the years, it was time for a more extensible framework addressing common pitfalls.

 - Identity Access Management
 - Supported Artifact Collection
 - API Call Exhaustion (Storage)

Enter the service, action, and result key to capture Amazon Web Services (AWS) data from that point in time view.

Reference: https://github.com/boto/botocore/tree/develop/botocore/data

### Installation

<details>
<summary>Requirement</summary>

AWS Command Line Interface (AWS CLI) Version 2

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

</details>

<details>
<summary>Deployment</summary>

```
pip install botoplus
```

</details>

<details>
<summary>Shell Completion</summary>

```
botoplus --install-completion
```

</details>

### IAM Identity Center 

<details>
<summary>Single Sign-On</summary>

```
$ botoplus login 
Identity Store: portal
SSO Region: us-east-2
SSO Role: AWSAdministratorAccess
Authenticated!!
```

</details>

### Pagination

<details>
<summary>Single Account - All Regions</summary>

```
$ botoplus account 
AWS Service: ec2
AWS Action: describe_instances
Result Key: Reservations
Selected Account: AccountName
** 123456789012 {AccountName} **
 - af-south-1
 - eu-north-1
 - ap-south-1
 - eu-west-3
 - eu-west-2
 - eu-south-1
 - eu-west-1
 - ap-northeast-3
 - ap-northeast-2
 - me-south-1
 - ap-northeast-1
 - me-central-1
 - sa-east-1
 - ca-central-1
 - ap-east-1
 - ap-southeast-1
 - ap-southeast-2
 - ap-southeast-3
 - eu-central-1
 - us-east-1
 - us-east-2
 - us-west-1
 - us-west-2
```

</details>

<details>
<summary>Single Region - All Accounts</summary>

```
$ botoplus paginator
AWS Service: ec2
AWS Action: describe_instances
Result Key: Reservations
Update Collection [y/N]: y
** 123456789011 {AccountName1} **
** 123456789012 {AccountName2} **
```

</details>

<details>
<summary>All Regions - All Accounts</summary>

```
$ botoplus paginators
AWS Service: ec2
AWS Action: describe_instances
Result Key: Reservations
** 123456789011 {AccountName1} **
 - af-south-1
 - eu-north-1
 - ap-south-1
 - eu-west-3
 - eu-west-2
 - eu-south-1
 - eu-west-1
 - ap-northeast-3
 - ap-northeast-2
 - me-south-1
 - ap-northeast-1
 - me-central-1
 - sa-east-1
 - ca-central-1
 - ap-east-1
 - ap-southeast-1
 - ap-southeast-2
 - ap-southeast-3
 - eu-central-1
 - us-east-1
 - us-east-2
 - us-west-1
 - us-west-2
** 123456789012 {AccountName2} **
 - af-south-1
 - eu-north-1
 - ap-south-1
 - eu-west-3
 - eu-west-2
 - eu-south-1
 - eu-west-1
 - ap-northeast-3
 - ap-northeast-2
 - me-south-1
 - ap-northeast-1
 - me-central-1
 - sa-east-1
 - ca-central-1
 - ap-east-1
 - ap-southeast-1
 - ap-southeast-2
 - ap-southeast-3
 - eu-central-1
 - us-east-1
 - us-east-2
 - us-west-1
 - us-west-2
```

</details>

<details>
<summary>Single Region - Single Account</summary>

```
$ botoplus region
AWS Service: ec2
AWS Action: describe_instances
Result Key: Reservations
Selected Account: AccountName
Selected Region: us-east-2 [y/N]: y
** 123456789012 {AccountName} **
 - us-east-2
```

</details>

### Validation

<details>
<summary>Items Checked</summary>

 - AWS Account Alias
 - AWS Account Number
 - Selected Account
 - Selected Region
 - SSO Active Region
 - SSO Active Role
 - Update Collection

</details>

### Development

<details>
<summary>Local Build</summary>

```
python setup.py install --user
```

</details>
