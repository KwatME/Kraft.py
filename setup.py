from os import walk
from os.path import abspath, dirname

from setuptools import setup

NAME = 'ccal'
URL = 'https://github.com/ucsd-ccal/ccal'
here = abspath(dirname(__file__))

packages = []
for dp, dns, fns in walk('../ccal'):
    if dp.split('/')[-1] not in ['.git', '__pycache__']:
        packages.append(dp)

setup(
    name=NAME,
    version='0.0.6',
    description=
    'Computational Cancer Analysis Library: bioinformatics library for hunting cancers',
    long_description='See {} for the documentation.'.format(URL),
    url=URL,
    author='Huwate \'Kwat\' Yeerna',
    author_email='kwatme8@gmail.com',
    license='LICENSE',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    keywords='Computational Cancer Analysis',
    packages=packages,
    python_requires='==3.6',
    install_requires=[
        'biopython==1.70',
        'matplotlib==2.1',
        'pandas==0.20',
        'scikit-learn==0.19',
        'scipy==0.19',
        'seaborn==0.8',
        'statsmodels==0.8',
    ],
    # And must install manually: $ conda install -c conda-forge rpy2 r-mass
    include_package_data=True)
