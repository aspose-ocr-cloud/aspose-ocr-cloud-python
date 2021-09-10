# coding: utf-8

from setuptools import setup, find_packages
from os import path

NAME = "aspose-ocr-cloud"
VERSION = "21.9.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "pyopenssl", "urllib3[secure]", "python-dateutil",
            "requests[security]"]

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description='Aspose.OCR Cloud SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Aspose',
    author_email='alexander.golshtein@aspose.com',
    url="https://products.aspose.cloud/ocr",
    license='MIT',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords=["Aspose.OCR Cloud API Reference", "Aspose", "OCR" "OCR Cloud"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
