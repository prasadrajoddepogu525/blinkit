from setuptools import find_packages,setup     # to pfind the packages in requirements.txt and setting up
from typing import List  # for hint the output will be in list format


# assign the .e - file to a variable
HYPEN_E_DOT='-e .'

def getting_requirements(file_path: str)->List[str]: #file path should be in string format and output will be in listformat
    """
    This function will return the list of elements

    """
    # we need to store the elements that found out from the file
    requirements=[]

    #opening the file
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='BLINKIT',
    version='0.0.1',
    description='This is BLINKIT',
    author='Prasadraj Oddepogu',
    author_email='prasadrajoddepogu525@gmail.com',
    packages=find_packages(),
    install_requires=getting_requirements('requirements.txt')
)