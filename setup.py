from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
    name='pubMunch3',
    version='1.0.3',
    description='A library and tool for downloading pubmed articles',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'beautifulsoup4==4.6',
        'unidecode==1.0.22',
        'incapsula-cracker-py3==0.1.8.1',
        'html5lib==1.0.1',
        'requests==2.25.1',
        'urllib3==1.26.4'
    ],

    package_data={
        'pubMunch': ['data/*']
    },

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'download_pmid=pubMunch:download_pmid_program',
        ],
    },
)
