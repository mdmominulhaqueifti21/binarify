from setuptools import setup, find_packages

setup(
    name="binarify",
    version="0.1.0",
    author="Md Mominul Haque Ifti",
    author_email="mdmominulhaqueifti21@gmail.com",
    description="Convert text and numbers to binary and back",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mdmominulhaqueifti21/binarify",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
