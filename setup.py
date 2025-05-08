from setuptools import setup, find_packages

setup(
    name='DeepAAV',
    version='0.1.0-alpha',
    packages=find_packages,
    install_requires=[
        'PySide6>=6.0',
        'biopython>=1.79',
        'biotite>=1.2.0',
    ],
    entry_points={
        'console_scripts' : [
            'DeepAAV = DeepAAV.main:main'
        ],
    },
)