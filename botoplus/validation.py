import aws_sso_lib
import boto3
import typer

def access(role,identity,region):

    roles = aws_sso_lib.list_available_roles(
        start_url = 'https://'+identity+'.awsapps.com/start',
        sso_region = region, 
        login = True
    )

    rolelist = []

    for account in roles:
        rolelist.append(account[2])

    unique = list(set(rolelist))

    if role not in unique:
        print('Role Access:')
        for item in unique:
            print(' * '+item)
        raise typer.Abort()

def accounts(selected_account,identity_store,sso_region):

    accounts = aws_sso_lib.list_available_accounts(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region, 
        login = True
    )
    
    accountlist = []

    for account in accounts:
        accountlist.append(account[0])

    if selected_account not in accountlist:
        print('Account List:')
        for account in accountlist:
            print(' * '+account)
        raise typer.Abort()

def active(region):

    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_regions()

    regionlist = []

    for regions in response['Regions']:
        regionlist.append(regions['RegionName'])

    if region not in regionlist:
        print('Active Regions:')
        for region in regionlist:
            print(' * '+region)
        raise typer.Abort()

def alias(selected_account,identity_store,sso_region):

    accounts = aws_sso_lib.list_available_accounts(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region, 
        login = True
    )

    for account in accounts:
        if account[1].lower() == selected_account.lower():
            item = {}
            item['awsaccount'] = account[0]
            item['awsalias'] = account[1]
            return item

    raise typer.Abort()
