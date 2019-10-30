# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='knnge',
    version='1.0.0',
    description='Holiday Gift Exchange Picker Using KNN',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Seth Black',
    author_email='sblack@sethserver.com',
    url='https://github.com/sethblack/knn-gift-exchange',
    license=license,
    packages=['knnge'],
    keywords=['knn', 'ai', 'unsupervised learning', 'random', 'artificial intelligence',],
    package_data={'knnge': ['uscities.csv',]},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'knnge=knnge.__main__:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    zip_safe=False,
)
