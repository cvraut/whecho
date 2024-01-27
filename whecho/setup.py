from setuptools import setup

setup(
    name='whecho',
    version='0.0.0',
    py_modules=['whecho'],
    entry_points={
        'console_scripts': [
            'whecho = whecho:main',
        ],
    },
)