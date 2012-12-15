import os
from setuptools import setup, find_packages
import unicodeblocks

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='unicodeblocks',
    version=unicodeblocks.version,
    description='Python module for unicode blocks',
    # long_description=read("README.md"),
    author='Simonas Kazlauskas',
    license="ISC",
    url='https://github.com/simukis/unicodeblocks',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities'
    ],
    zip_safe=False,
)
