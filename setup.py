'''
The setup.py file ia an essential part of packaging and distributing python projects .
it is usedby setuptools to define the configuration of your project, such as 
metadata,dependencies, and more 
'''

from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    try:
        requirement_lst:List[str]=[]
        with open(file_path,"r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file is not found")
    return requirement_lst


setup(
    name="Network security",
    version="0.0.1",
    author='Gopi',
    author_email='n210204@rguktn.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)







