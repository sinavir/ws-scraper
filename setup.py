from setuptools import setup

setup(
    name='ws_scraper',
    version='0.1',
    packages=['ws_scraper'],
    install_requires=[
        'websockets',
        'aiosqlite',
    ],
    entry_points={
        'console_scripts': [
            'ws-scraper = ws_scraper:main',
        ],
    },
)
