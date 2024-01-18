from setuptools import find_packages, setup
from typing import List

editable_entry = '-e .'

def get_requirements(filepath: str) -> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

    # Exclude the editable entry if present
    requirements = [req for req in requirements if req != editable_entry]

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='vineetkukreti',
    author_email='vineetkukreti34@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    package_data={'mlproject': ['data/*.csv', 'models/*.h5']},
)
