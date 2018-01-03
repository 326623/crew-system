from setuptools import setup

setup(
    name='crewmen',
    author='Newjoy',
    author_email='yangqp5@mail2.sysu.edu.cn',
    license='GPLv3',
    version='0.1',
    description='crew management web application',
    packages=['crewmen'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
