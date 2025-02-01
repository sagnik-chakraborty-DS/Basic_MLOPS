"""
This will help us to use
my ml application as package
"""
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    This function will read the requirements.txt file and return the list of requirements
    """
    with open(file_path,'r') as file:
        requirements = file.read().splitlines()
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        print(requirements)    
        return  requirements



setup(
    name='ml_app-MLOPS',
    packages=find_packages(),# it will find packages how many directory have __init__.py file
    version='0.1.0',
    author='Sagnik Chakraborty',
    author_email="sagnikc137@gmail.com",
    license='Apache',
    # install_requires=[
    #     'pandas',
    #     'numpy',
    #     'seaborn',
    # ]
    install_requires=get_requirements('requirements.txt'),
)