from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine_Learning_Modular_Programming"
VERSION = "0.0.1"
DESCRIPTION = "This project is for modular programming in Python and MLOps"
AUTHOR_NAME = "Shashank Chhoker"
AUTHOR_EMAIL = "shashanksaad07@gmail.com"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

# Read the requirement file and return a list of dependencies
def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME, "r") as file:
        requirements_list = file.readlines()  # Corrected variable name
        requirements_list = [requirement.strip() for requirement in requirements_list]  # Removing \n
        
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
    
    return requirements_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements_list(),  # Call function to get requirements list
)
