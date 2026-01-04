from setuptools import find_packages,setup
from typing import List

def get_requirements()->list[str]:
    """
    Docstring for get_requirements
    
    This function will return list of requirements
    """
    req_list:List[str]=[]
    try:
        with open('req.txt','r') as file:
            lines=file.readlines()

            for line in lines:
                req=line.strip()
                if req and req != '-e .':
                    req_list.append(req)
    except FileNotFoundError:
        print("req.txt not found")

    return req_list

# print(get_requirements())


setup(
    name="NetworkSecurity",
    version='0.0.1',
    author="Anmol Jain",
    author_email='anmol752005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)