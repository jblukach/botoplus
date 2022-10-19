from setuptools import setup

from botoplus import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name = "botoplus",
    version = __version__,
    description = "tba",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/botoplus/botoplus",
    author = "botoplus",
    author_email = "hello@botoplus.com",
    license = "Apache-2.0",
    packages = ["botoplus"],
    zip_safe = False,
    entry_points = {
        "console_scripts": ["botoplus=botoplus.botoplus:main"],
    },
    python_requires = ">=3.7",
)