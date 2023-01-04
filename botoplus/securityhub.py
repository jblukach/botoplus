import aws_sso_lib
import boto3
import datetime
import pathlib
import typer
import botoplus.validation as _valid

app = typer.Typer()

@app.command()
def baseline():

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    sso_region = pathlib.Path(sso).read_text()

    role = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_role')
    sso_role = pathlib.Path(role).read_text()

    confirm = typer.confirm("Configure")

    if not confirm:

        raise typer.Abort()

    accounts = aws_sso_lib.list_available_accounts(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region, 
        login = True
    )

    for account in accounts:

        try:

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

            print('** '+account[0]+' {'+account[1]+'} **')

            for regions in response['Regions']:

                try:

                    try:

                        securityhub = session.client('securityhub', region_name = regions['RegionName'])

                        paginator = securityhub.get_paginator('get_enabled_standards')

                        pages = paginator.paginate()

                        for page in pages:
                            for subscriptions in page['StandardsSubscriptions']:
                                securityhub.batch_disable_standards(
                                    StandardsSubscriptionArns = [
                                        subscriptions['StandardsSubscriptionArn']
                                    ]
                                )

                    except:
                        pass

                    try:

                        paginator = securityhub.get_paginator('list_enabled_products_for_import')

                        pages = paginator.paginate()

                        for page in pages:
                            for products in page['ProductSubscriptions']:
                                parsed = products.split('/')
                                if parsed[2] != 'access-analyzer' and \
                                  parsed[2] != 'health' and parsed[2] != 'securityhub':
                                    securityhub.disable_import_findings_for_product(
                                        ProductSubscriptionArn = products
                                    )

                    except:
                        pass

                    print(' - '+regions['RegionName'])

                except:
                    print(' - '+regions['RegionName']+' DENIED')
                    pass

        except:
            print('** '+account[0]+' {'+account[1]+'} ** DENIED')
            pass

if __name__ == "__main__":
    app()
