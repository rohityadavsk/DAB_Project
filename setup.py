from setuptools import setup, find_packages

setup(
    name="rohit_dab_project",
    version="0.0.3",
    description='This contains the code in the ./src directory of the DAB project.',
    author="Rohit",
    packages=find_packages(where='./src'),
    package_dir={'': './src'},
    install_requires=['setuptools'],
    entry_points={
        'packages': [
            "main=rohit_dab_project.main:main"
        ]
    }
)