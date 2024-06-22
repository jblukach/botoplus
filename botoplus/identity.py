import aws_sso_lib
import pathlib
import typer

def login():

    ### previous login ###

    idp = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    role = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_role')
    cli = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_cli')
    out = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_output')

    ### identity provider ###

    if idp.is_file() == False:

        identity_store = typer.prompt("Identity Store").strip()
        pathlib.Path(idp).write_text(identity_store)

    else:

        identity_store = pathlib.Path(idp).read_text()
        correct = typer.confirm("Identity Store {"+identity_store+"}")

        if not correct:

            identity_store = typer.prompt("Identity Store").strip()
            pathlib.Path(idp).write_text(identity_store)

    ### sso region ###

    if sso.is_file() == False:

        sso_region = typer.prompt("SSO Region").strip()
        pathlib.Path(sso).write_text(sso_region)

    else:

        sso_region = pathlib.Path(sso).read_text()
        correct = typer.confirm("SSO Region {"+sso_region+"}")

        if not correct:

            sso_region = typer.prompt("SSO Region").strip()
            pathlib.Path(sso).write_text(sso_region)

    ### sso login ###

    login = aws_sso_lib.login(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region
    )

    ### sso role ###

    if role.is_file() == False:

        sso_role = typer.prompt("SSO Role").strip()
        pathlib.Path(role).write_text(sso_role)

    else:

        sso_role = pathlib.Path(role).read_text()
        correct = typer.confirm("SSO Role {"+sso_role+"}")

        if not correct:

            sso_role = typer.prompt("SSO Role").strip()
            pathlib.Path(role).write_text(sso_role)

    ### cli region ###

    if cli.is_file() == False:

        cli_region = typer.prompt("CLI Region").strip()
        pathlib.Path(cli).write_text(cli_region)

    else:

        cli_region = pathlib.Path(cli).read_text()
        correct = typer.confirm("CLI Region {"+cli_region+"}")

        if not correct:

            cli_region = typer.prompt("CLI Region").strip()
            pathlib.Path(cli).write_text(cli_region)

    ### cli output ###

    if out.is_file() == False:

        cli_output = typer.prompt("CLI Output").strip()
        pathlib.Path(out).write_text(cli_output)

    else:

        cli_output = pathlib.Path(out).read_text()
        correct = typer.confirm("CLI Output {"+cli_output+"}")

        if not correct:

            cli_output = typer.prompt("CLI Output").strip()
            pathlib.Path(out).write_text(cli_output)

    ### configuration ###
    
    config = pathlib.Path.joinpath(pathlib.Path.home(),'.aws','config')
    pathlib.Path(config).parents[0].mkdir(parents = True, exist_ok = True)
    
    accounts = aws_sso_lib.list_available_accounts(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region, 
        login = True
    )

    f = pathlib.Path(config).open('w')

    for account in accounts:
        
        alias = account[1].replace(' ','')

        f.write('[profile '+alias+']\n')
        f.write('credential_process = aws-sso-util credential-process --profile '+alias+'\n')
        f.write('sso_start_url = https://'+identity_store+'.awsapps.com/start\n')    
        f.write('sso_region = '+sso_region+'\n')
        f.write('sso_account_id = '+account[0]+'\n')
        f.write('sso_role_name = '+sso_role+'\n')
        f.write('region = '+cli_region+'\n')
        f.write('output = '+cli_output+'\n\n')

    f.close()

    print('Logged In!!')

def logout():

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    identity_store = pathlib.Path(identity).read_text()

    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    sso_region = pathlib.Path(sso).read_text()

    aws_sso_lib.sso.logout(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region,
        sso_cache = None
    )

    print('Logged Out!!')
