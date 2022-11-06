import aws_sso_lib
import pathlib
import typer
import botoplus.validation as _valid

def login():

    identity = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_idp')
    sso = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_sso')
    role = pathlib.Path.joinpath(pathlib.Path.home(),'.botoplus_role')

### identity ###

    if identity.is_file() == False:

        identity_store = typer.prompt("Identity Store").strip()
        pathlib.Path(identity).write_text(identity_store)

    else:

        identity_store = pathlib.Path(identity).read_text()
        correct = typer.confirm("Identity Store {"+identity_store+"}")

        if not correct:

            identity_store = typer.prompt("Identity Store").strip()
            pathlib.Path(identity).write_text(identity_store)

### sso region ###

    if sso.is_file() == False:

        sso_region = typer.prompt("SSO Region").strip()
        _valid.active(sso_region)
        pathlib.Path(sso).write_text(sso_region)

    else:

        sso_region = pathlib.Path(sso).read_text()
        correct = typer.confirm("SSO Region {"+sso_region+"}")

        if not correct:

            sso_region  = typer.prompt("SSO Region").strip()
            _valid.active(sso_region)
            pathlib.Path(sso).write_text(sso_region)

### sso login ###

    login = aws_sso_lib.login(
        start_url = 'https://'+identity_store+'.awsapps.com/start',
        sso_region = sso_region, 
        disable_browser = True
    )

### sso role ###

    if role.is_file() == False:

        sso_role = typer.prompt("SSO Role").strip()
        _valid.access(sso_role, identity_store, sso_region)
        pathlib.Path(role).write_text(sso_role)

    else:

        sso_role = pathlib.Path(role).read_text()
        correct = typer.confirm("SSO Role {"+sso_role+"}")

        if not correct:

            sso_role  = typer.prompt("SSO Role").strip()
            _valid.access(sso_role, identity_store, sso_region)
            pathlib.Path(role).write_text(sso_role)

    print('Authenticated!!')
