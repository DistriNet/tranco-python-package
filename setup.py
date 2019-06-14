import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tranco",
    version="0.3",
    author="Victor Le Pochat",
    author_email="victor.lepochat@cs.kuleuven.be",
    description="Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DistriNet/tranco-python-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests'
    ]
)