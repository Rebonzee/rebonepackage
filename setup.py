from setuptools import setup, find_packages

setup(
    name='rebonepackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/rebonepackage',
    author='Rebonemokome',
    author_email='ribsmokome@live.co.za'
)
