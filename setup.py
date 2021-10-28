"""python3-vagrant setup"""

import os
import re
from setuptools import setup

# parse version from package/module without importing or evaluating the code
with open("vagrant/__init__.py", encoding="utf-8") as fh:
    for line in fh:
        m = re.match(r"^__version__ = .*\"$", line)
        if m:
            version = re.split(" ", line)[2].rstrip().strip('"')
            break

setup(
    name="python3-vagrant",
    version=version,
    license="MIT",
    description="Python bindings for interacting with Vagrant virtual machines.",
    long_description=open(
        os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8"
    ).read(),
    keywords="python virtual machine box vagrant virtualbox vagrantfile",
    url="https://github.com/konstruktoid/python3-vagrant",
    author="Thomas Sjögren",
    author_email="konstruktoid@users.noreply.github.com",
    # url="https://github.com/todddeluca/python-vagrant",
    # author="Todd Francis DeLuca",
    # author_email="todddeluca@yahoo.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["vagrant"],
)
