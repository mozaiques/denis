from setuptools import setup


description = (
    'A thin set of abstractions to perform geometrical operations on '
    'top of the latitude/longitude coordinate system'
)


setup(
    name='denis',
    version='0.0.7',
    description=description,
    url='https://github.com/mozaiques/denis',
    author='Bastien Gandouet',
    author_email='bastien@mozaiqu.es',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['denis'],
    install_requires=['numpy', 'cffi>=1.10'],
    include_package_data=True,
    zip_safe=False,
)
