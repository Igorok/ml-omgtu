# pip install -e .

from setuptools import setup, find_packages

setup(
    name='ml-omgu',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'sympy',
    ],
    # py_modules=['rcviz'],
)