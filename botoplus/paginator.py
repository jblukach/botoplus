import aws_sso_lib
import datetime
import pathlib
import typer
import botoplus.validation as _valid

def paginator(service,action,key):

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    sso_region = pathlib.Path(sso).read_text()

    role = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_role')
    sso_role = pathlib.Path(role).read_text()

    correct = typer.confirm("Selected Region: "+sso_region)

    if not correct:

        selected_region  = typer.prompt("Selected Region").strip()
        _valid.active(selected_region)

    else:

        selected_region = sso_region

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

        try:

            session = aws_sso_lib.get_boto3_session(
                start_url = 'https://'+identity_store+'.awsapps.com/start',
                sso_region = sso_region, 
                account_id = account[0],
                role_name = sso_role,
                region  = selected_region,
                login = True
            )

            print('** '+account[0]+' {'+account[1]+'} **')

            client = session.client(service)

            paginator = client.get_paginator(action)

            pages = paginator.paginate()

            for page in pages:

                for item in page[key]:

                    item['awsaccount'] = account[0]
                    item['awsalias'] = account[1]
                    f.write(str(item)+'\n')

        except:

            print('** '+account[0]+' {'+account[1]+'} ** DENIED')
            pass

    f.close()
