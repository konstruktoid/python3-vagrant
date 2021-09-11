import os
import re
from setuptools import setup

# parse version from package/module without importing or evaluating the code
with open("vagrant/__init__.py") as fh:
    for line in fh:
        m = re.search(r"^__version__ = '(?P<version>[^']+)'$", line)
        if m:
            version = m.group("version")
            break

setup(
    name="python3-vagrant",
    version=version,
    license="MIT",
    description="Python bindings for interacting with Vagrant virtual machines.",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
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
