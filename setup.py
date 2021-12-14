from setuptools import setup, find_packages

setup(
    name='ml-omgu',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas'
    ],
    # py_modules=['rcviz'],
)