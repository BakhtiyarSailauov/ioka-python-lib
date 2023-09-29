from setuptools import setup, find_packages

setup(
    name='ioka-python-lib',
    version='0.8.0',
    packages=find_packages(),
    url='https://github.com/BakhtiyarSailauov/ioka-python-lib',
    author='Bakhtiyar Sailauov',
    author_email='cena61454@gmail.com',
    description='A Python library for interacting with the Ioka API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.26.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
