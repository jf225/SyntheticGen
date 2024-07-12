from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'Synthetic dataset creator/augmentor for machine learning applications.'

# Setting up
setup(
    name="SyntheticGen",
    version=VERSION,
    author="James Fahey",
    author_email="<jamesaf36@gmail.com>",
    url='https://github.com/jf225/SyntheticGen',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy >= 1.26.1'],
    license="MIT",
    keywords=['python', 'machine learning', 'data augmentation', 'sythetic datasets'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)