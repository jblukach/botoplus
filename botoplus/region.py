import aws_sso_lib
import datetime
import pathlib
import typer
import botoplus.validation as _valid

def region(service,action,key):

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    sso_region = pathlib.Path(sso).read_text()

    role = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_role')
    sso_role = pathlib.Path(role).read_text()

    selected_account  = typer.prompt("Selected Account").strip()
    
    if len(selected_account) == 12 and selected_account.isdigit():

        _valid.accounts(selected_account,identity_store,sso_region)

    else:
        
        selected_account = _valid.alias(selected_account,identity_store,sso_region)

    correct = typer.confirm("Selected Region: "+sso_region)

    if not correct:

        selected_region  = typer.prompt("Selected Region")
        _valid.active(selected_region)

    else:

        selected_region = sso_region

    storage = pathlib.Path.joinpath(pathlib.Path.home(),'botoplus',service,action+'.txt')
    pathlib.Path(storage).parents[0].mkdir(parents = True, exist_ok = True)

    if storage.is_file():

        timestamp = datetime.datetime.fromtimestamp(pathlib.Path(storage).stat().st_mtime)

        print('Last Modified: '+str(timestamp))

        update = typer.confirm("Update Collection")

        if not update:

            raise typer.Abort()

    f = pathlib.Path(storage).open('w')

    print('** '+selected_account['awsaccount']+' {'+selected_account['awsalias']+'} **')

    try:

        session = aws_sso_lib.get_boto3_session(
            start_url = 'https://'+identity_store+'.awsapps.com/start',
            sso_region = sso_region, 
            account_id = selected_account['awsaccount'],
            role_name = sso_role,
            region  = selected_region,
            login = True
        )

        print(' - '+selected_region)

        client = session.client(service)

        paginator = client.get_paginator(action)

        pages = paginator.paginate()

        for page in pages:

            for item in page[key]:

                item['awsaccount'] = selected_account['awsaccount']
                item['awsalias'] = selected_account['awsalias']
                f.write(str(item)+'\n')

    except:
        print(' - '+selected_region+' DENIED')
        pass

    f.close()
