from setuptools import setup, find_packages


setup(
    name='denis',
    version='0.0.1',
    description='A sample Python project',
    url='https://github.com/mozaiques/denis',
    author='Bastien Gandouet',
    author_email='bastien@mozaiqu.es',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=['numpy'],
)
