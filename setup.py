from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filename: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(filename) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]  # Corrected line
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ml_projects',
    version='0.0.1',
    author='NaveenK389',
    author_email='kattanaveen202@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
