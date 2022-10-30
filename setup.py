from setuptools import setup

setup(
    name='ws_scrapper',
    version='1.0',
    packages=['ws_scrapper'],
    install_requires=[
        'websockets',
    ],
    entry_points={
        'console_scripts': [
            'ws-scrapper = ws_scrapper:main',
        ]
    }
)
