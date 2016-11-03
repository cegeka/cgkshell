from setuptools import setup, find_packages

setup(
    name='CgkShell',
    version='0.0.1.0',
    author='Rial Juan',
    author_email='<jrial@safehex.be>',
    description='Tools for interacting with the shell',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='shell',
    url='https://github.com/cegeka/cgkshell/',

    # package source directory
    package_dir={'': 'src'},
    packages=find_packages('src', exclude='docs')
)
