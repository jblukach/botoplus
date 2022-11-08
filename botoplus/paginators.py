import aws_sso_lib
import boto3
import datetime
import pathlib
import typer
import botoplus.validation as _valid

def paginators(service,action,key):

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    sso_region = pathlib.Path(sso).read_text()

    role = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_role')
    sso_role = pathlib.Path(role).read_text()

    accounts = aws_sso_lib.list_available_accounts(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region, 
        login = True
    )

    storage = pathlib.Path.joinpath(pathlib.Path.home(),'botoplus',service,action+'.txt')
    pathlib.Path(storage).parents[0].mkdir(parents = True, exist_ok = True)

    if storage.is_file():

        timestamp = datetime.datetime.fromtimestamp(pathlib.Path(storage).stat().st_mtime)

        print('Last Modified: '+str(timestamp))

        update = typer.confirm("Update Collection")

        if not update:

            raise typer.Abort()

    f = pathlib.Path(storage).open('w')

    for account in accounts:

        print('** '+account[0]+' {'+account[1]+'} **')

        session = aws_sso_lib.get_boto3_session(
            start_url = 'https://'+identity_store+'.awsapps.com/start',
            sso_region = sso_region, 
            account_id = account[0],
            role_name = sso_role,
            region  = sso_region,
            login = True
        )

        ec2_global = session.client('ec2')

        response = ec2_global.describe_regions()

        for regions in response['Regions']:

            try:

                print(' - '+regions['RegionName'])

                ec2_client = session.client(service, region_name = regions['RegionName'])

                paginator = ec2_client.get_paginator(action)
    
                pages = paginator.paginate()

                for page in pages:

                    for item in page[key]:

                        item['awsaccount'] = account[0]
                        item['awsalias'] = account[1]
                        f.write(str(item)+'\n')

            except:
                print(' - '+regions['RegionName']+' DENIED')
                pass

    f.close()
