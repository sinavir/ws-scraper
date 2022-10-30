from setuptools import setup

setup(
    name='ws_scrapper',
    version='0.1',
    packages=['ws_scrapper'],
    install_requires=[
        'websockets',
        'aiosqlite',
    ],
    entry_points={
        'console_scripts': [
            'ws-scrapper = ws_scrapper:main',
        ],
    },
)
