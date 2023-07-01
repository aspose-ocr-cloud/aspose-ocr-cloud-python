# coding: utf-8

"""
    Aspose OCR Cloud 5.0 API

    Aspose OCR Cloud 5.0 API  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "aspose-ocr-cloud"
VERSION = "23.6.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="Aspose OCR Cloud 5.0 API",
    author="Aspose",
    author_email="",
    url="https://pypi.org/project/aspose-ocr-cloud/",
    keywords=["Aspose", "OCR", "Aspose OCR Cloud 5.0 API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=long_description
)
