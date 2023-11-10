import aws_sso_lib
import pathlib
import typer

def account(selected_account,identity_store,sso_region):

    accounts = aws_sso_lib.list_available_accounts(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region, 
        login = True
    )
    
    for account in accounts:
        if account[0] == selected_account:
            item = {}
            item['awsaccount'] = account[0]
            item['awsalias'] = account[1]
            return item

    raise typer.Abort()

def accounts():

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_sso')
    sso_region = pathlib.Path(sso).read_text()

    accounts = aws_sso_lib.list_available_accounts(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region, 
        login = True
    )

    acctlist = []

    for account in accounts:
        acct = {}
        acct['awsaccount'] = account[0]
        acct['awsalias'] = account[1]
        acctlist.append(acct)

    return acctlist

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

def convert(selected_account):

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_sso')
    sso_region = pathlib.Path(sso).read_text()

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

def default():

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_sso')
    sso_region = pathlib.Path(sso).read_text()

    role = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_role')
    sso_role = pathlib.Path(role).read_text()

    selected_account  = typer.prompt("Selected Account").strip()
    print(' '+selected_account+'\n')

    if len(selected_account) == 12 and selected_account.isdigit():
        selected_account = account(selected_account,identity_store,sso_region)
    else:    
        selected_account = alias(selected_account,identity_store,sso_region)

    try:
        session = aws_sso_lib.get_boto3_session(
            start_url = 'https://'+identity_store+'.awsapps.com/start',
            sso_region = sso_region, 
            account_id = selected_account['awsaccount'],
            role_name = sso_role,
            region  = sso_region,
            login = True
        )
        return session
    except:
        print('\n** '+selected_account['awsaccount']+' {'+selected_account['awsalias']+'} - DENIED **')
        pass

def defaults(selected_account):

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_sso')
    sso_region = pathlib.Path(sso).read_text()

    role = pathlib.Path.joinpath(pathlib.Path.home(),'.aqueduct_role')
    sso_role = pathlib.Path(role).read_text()

    if len(selected_account) == 12 and selected_account.isdigit():
        selected_account = account(selected_account,identity_store,sso_region)
    else:    
        selected_account = alias(selected_account,identity_store,sso_region)

    try:
        session = aws_sso_lib.get_boto3_session(
            start_url = 'https://'+identity_store+'.awsapps.com/start',
            sso_region = sso_region, 
            account_id = selected_account['awsaccount'],
            role_name = sso_role,
            region  = sso_region,
            login = True
        )
        return session
    except:
        print('\n** '+selected_account['awsaccount']+' {'+selected_account['awsalias']+'} - DENIED **')
        pass

def execution():
    query_execution_id  = typer.prompt("Query Execution Id").strip()
    print(' '+query_execution_id+'\n')
    return query_execution_id

def hello():
    print('Hello, World!')
