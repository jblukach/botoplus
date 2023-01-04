import aws_sso_lib
import boto3
import datetime
import pathlib
import typer
import botoplus.validation as _valid

app = typer.Typer()

@app.command()
def deletestack():

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    sso_region = pathlib.Path(sso).read_text()

    role = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_role')
    sso_role = pathlib.Path(role).read_text()

    stack_name = typer.prompt("Stack Name").strip()

    confirm = typer.confirm("Destroy")

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

                        cfn_client = session.client('cloudformation', region_name = regions['RegionName'])

                        cfn_client.update_termination_protection(
                            EnableTerminationProtection = False,
                            StackName = stack_name
                        )

                        cfn_client.delete_stack(
                            StackName = stack_name
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
