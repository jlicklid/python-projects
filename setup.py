from setuptools import setup, find_packages


with open('README.md') as f:
    readme_text = f.read()

with open('LICENSE') as f:
    license_text = f.read()

setup(
    name='nltk-cookbook',
    version='0.0.1',
    description='setting up virtual environment',
    long_description=readme_text,
    author='Joel Licklider',
    author_email='ghoal3@gmail.com',
    url='https://github.com/ghoal/python-projects',
    license=license_text,
    packages=find_packages(exclude=('tests',))
)
