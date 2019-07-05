import click
import requests
import json

setup(
    name = '16x16',
    version = '0.1.0',
    packages = ['click','requests', 'json'],
    entry_points = {
        'console_scripts': [
            '16x16 = cli-controller.__main__:main'
        ]
    })
