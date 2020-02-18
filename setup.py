from setuptools import setup, find_packages

setup(
    name='analyse',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA data analysis project',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/OGSEQEBO/analyse.git',
    author='Otshepahetse Seqebo',
    author_email='ogseqebo@gmail.com'
)