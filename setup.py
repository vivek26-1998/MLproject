from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will retutn list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]





setup(
name='mlproject',
version = '0.0.1',
author='Vivek',
author_email='vivekharidask@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)