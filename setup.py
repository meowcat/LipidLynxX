from io import IncrementalNewlineDecoder
from setuptools import setup, find_packages
from glob import glob
import pathlib

f = open('requirements.txt', 'r')
req = f.readlines()
req = [r.replace('\n', '') for r in req]
# https://github.com/maet3608/minimal-setup-py/blob/master/setup.py


def get_files(dir):
    return [str(x) for x in pathlib.Path(dir).iterdir() if x.is_file()]


setup(
    name='lipidlynxx',
    version='0.0.1',
    url='https://github.com/SysMedOs/LipidLynxX',
    author='Zhixu Ni, Maria Fedorova',
    author_email='author@gmail.com',
    description='LipidLynxx',
    packages=find_packages(exclude=('test')),    
    install_requires=req,
    include_package_data = True
)
