from setuptools import setup,find_packages
from typing import List

## declaring variables for the setup
PROJECT_NAME = 'housing-predictor'
AUTHOR = 'Praveen Hosamani'
VERSION = '0.0.6'
DESCRIPTION = 'This i my first full stack ML project'
#PACKAGES = ['housing']

def get_requirements_list()->List[str]: # returns list of strings
    """
    Description: This function is going to return list of libraries mentioned 
    in the requirements.txt

    returns: list of libraries mentioned in the requirements.txt  
    """
    with open('requirements.txt','r') as f:
        return f.readlines().remove("-e .")
        # -e . installs all the libraries inside the housing folder or packages
        # pip install without -e . in  req.txt wont install the packages
        # and its removed because we use find_packages() which includes the all packages
        # setup.py file is must before installing -e .

setup(
    name= PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), # finds all folders in which __init__ present
    install_requires = get_requirements_list()
)


