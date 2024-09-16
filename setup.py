from setuptools import find_namespace_packages, setup
from typing import List

HYPEN_E_DOT ='-e.'
def get_requirements(file_path:str)->List[str]:
    ''' This function will return the list of requirments '''
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'deeplearning',
    version= '1.0',
    author= "Nahid Ferdous",
    author_email= "Nahid.mferdous@gmail.com",
    packages= find_namespace_packages(),
    install_requires = get_requirements('requirements.txt')
)