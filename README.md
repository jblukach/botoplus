# botoplus

### Install

```
pip install botoplus
```

### Login

```
$ botoplus login 
Identity Store: portal
SSO Region: us-east-2
SSO Role: AWSAdministratorAccess
Authenticated!!
```

### Account

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

### Paginator

```
$ botoplus paginator
AWS Service: ec2
AWS Action: describe_instances
Result Key: Reservations
Selected Region: us-east-2 [y/N]: y
Last Modified: 2022-11-06 22:58:45.313488
Update Collection [y/N]: y
** 123456789011 {AccountName1} **
** 123456789012 {AccountName2} **
```

### Paginators

```
$ botoplus paginators
AWS Service: ec2
AWS Action: describe_instances
Result Key: Reservations
Last Modified: 2022-11-06 22:58:45.313488
Update Collection [y/N]: y
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

### Region

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

### Local Development

```
python setup.py install --user
```
