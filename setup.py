from setuptools import setup, find_packages

setup(
    name='CgkShell',
    version='0.0.1.0',
    author='Rial Juan <jrial@safehex.be>',
    description='Tools for interacting with the shell',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords="shell",

    # package source directory
    package_dir={'': 'src'},
    packages=find_packages('src', exclude='docs')
)
