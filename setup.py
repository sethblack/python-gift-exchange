# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.md') as f:
    readme = f.read()

setup(
    name='pyge',
    version='1.0.0',
    description='Python Gift Exchange Picker',
    long_description_content_type='text/markdown',
    long_description='Python Gift',
    author='Seth Black',
    author_email='sblack@sethserver.com',
    url='https://github.com/sethblack/knn-gift-exchange',
    license='Apache Software License',
    packages=['pyge'],
    keywords=['ai', 'unsupervised learning', 'random', 'artificial intelligence', 'secret santa', 'gift exchange',],
    package_data={'pyge': ['uscities.csv',]},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pyge=pyge.__main__:main',
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
