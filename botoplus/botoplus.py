import pathlib
import typer
import botoplus.account as _account
import botoplus.cdk as _cdk
import botoplus.cloudformation as _cloudformation
import botoplus.identity as _idp
import botoplus.paginator as _page
import botoplus.paginators as _pages
import botoplus.region as _region
import botoplus.securityhub as _securityhub

app = typer.Typer()

@app.command()
def account():
    aws_service = typer.prompt("AWS Service").strip()
    aws_action = typer.prompt("AWS Action").strip()
    result_key = typer.prompt("Result Key").strip()
    _account.account(aws_service,aws_action,result_key)

app.add_typer(_cdk.app, name='cdk')

app.add_typer(_cloudformation.app, name='cloudformation')

@app.command()
def login():
    _idp.login()

@app.command()
def logout():
    _idp.logout()

@app.command()
def paginator():
    aws_service = typer.prompt("AWS Service").strip()
    aws_action = typer.prompt("AWS Action").strip()
    result_key = typer.prompt("Result Key").strip()
    _page.paginator(aws_service,aws_action,result_key)

@app.command()
def paginators():
    aws_service = typer.prompt("AWS Service").strip()
    aws_action = typer.prompt("AWS Action").strip()
    result_key = typer.prompt("Result Key").strip()
    _pages.paginators(aws_service,aws_action,result_key)

@app.command()
def region():
    aws_service = typer.prompt("AWS Service").strip()
    aws_action = typer.prompt("AWS Action").strip()
    result_key = typer.prompt("Result Key").strip()
    _region.region(aws_service,aws_action,result_key)

app.add_typer(_securityhub.app, name='securityhub')

if __name__ == "__main__":
    app()
