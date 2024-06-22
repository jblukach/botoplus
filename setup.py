from setuptools import setup

from botoplus import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "botoplus",
    version = __version__,
    description = "Python Library for Jupyter Notebooks that provides Security Operations the Threat Detection and Response capabilities needed during an Amazon Web Services (AWS) investigation.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jblukach/botoplus",
    author = "John Lukach",
    author_email = "hello@lukach.io",
    license = "Apache-2.0",
    packages = ["botoplus"],
    install_requires = [
        "aws-sso-lib",
        "boto3",
        "typer"
    ],
    python_requires = ">=3.8",
)