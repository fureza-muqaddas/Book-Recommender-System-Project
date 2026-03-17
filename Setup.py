from setuptools import setup, find_packages
from typing import List



def get_requirements(file_path: str) -> List[str]:
    requirements=[]

    with open(file_path, 'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    return requirements

setup(
    name='ds_project',
    version='0.1',
    author='Fureza Muqaddas',
    author_email='furezamuqaddas@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)