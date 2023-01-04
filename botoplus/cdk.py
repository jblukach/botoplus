import aws_sso_lib
import boto3
import datetime
import pathlib
import typer
import botoplus.validation as _valid

app = typer.Typer()

@app.command()
def unbootstrap():

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    sso_region = pathlib.Path(sso).read_text()

    role = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_role')
    sso_role = pathlib.Path(role).read_text()

    cdk_qualifier = typer.prompt("CDK Qualifier").strip()

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

                        ecr = 'cdk-'+cdk_qualifier+'-container-assets-'+account[0]+'-'+regions['RegionName']

                        ecr_client = session.client('ecr', region_name = regions['RegionName'])

                        paginator = ecr_client.get_paginator('list_images')

                        pages = paginator.paginate(
                            repositoryName = ecr
                        )

                        for page in pages:
                            for image in page['imageIds']:
                                ecr_client.batch_delete_image(
                                    repositoryName = ecr,
                                    imageIds = [
                                        {
                                            'imageDigest': image['imageDigest'],
                                            'imageTag': image['imageTag']
                                        }
                                    ]
                                )

                    except:
                        pass

                    bucket = 'cdk-'+cdk_qualifier+'-assets-'+account[0]+'-'+regions['RegionName']

                    s3_client = session.client('s3')

                    try:

                        paginator = s3_client.get_paginator('list_objects_v2')

                        pages = paginator.paginate(
                            Bucket = bucket
                        )

                        for page in pages:
                            for object in page['Contents']:
                                s3_client.delete_object(
                                    Bucket = bucket,
                                    Key = object['Key']
                                )

                    except:
                        pass

                    try:

                        paginator = s3_client.get_paginator('list_object_versions')

                        pages = paginator.paginate(
                            Bucket = bucket
                        )

                        for page in pages:
                            for object in page['Versions']:
                                s3_client.delete_object(
                                    Bucket = bucket,
                                    Key = object['Key'],
                                    VersionId = object['VersionId']
                                )

                        for page in pages:
                            for object in page['DeleteMarkers']:
                                s3_client.delete_object(
                                    Bucket = bucket,
                                    Key = object['Key'],
                                    VersionId = object['VersionId']
                                )

                    except:
                        pass

                    try:
                        s3_client.delete_bucket(
                            Bucket = bucket
                        )
                    except:
                        pass

                    try:

                        cfn = 'cdk-bootstrap-'+cdk_qualifier+'-'+account[0]+'-'+regions['RegionName']

                        cfn_client = session.client('cloudformation', region_name = regions['RegionName'])

                        cfn_client.update_termination_protection(
                            EnableTerminationProtection = False,
                            StackName = cfn
                        )

                        cfn_client.delete_stack(
                            StackName = cfn
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
