#!/usr/bin/env python
"""ETI/Domo integration library setup."""

import re
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """PyTest controller."""

    # Code from here:
    # https://docs.pytest.org/en/latest/goodpractices.html#manual-integration

    # pylint: disable=attribute-defined-outside-init
    def finalize_options(self):
        """Finalize test command options."""
        TestCommand.finalize_options(self)
        # we don't run integration tests which need an actual CAME device
        self.test_args = ["-m", "not integration"]
        self.test_suite = True

    # pylint: disable=import-outside-toplevel,import-error
    def run_tests(self):
        """Run tests."""
        # import here, cause outside the eggs aren't loaded
        import shlex

        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


def load_requirements(fpath: str) -> list:
    """Load requirements from file."""
    data = list(open(fpath))
    imp = re.compile(r"^(-r|--requirement)\s+(\S+)")
    reqs = []
    for i in data:
        # pylint: disable=invalid-name
        m = imp.match(i)
        if m:
            reqs.extend(load_requirements(m.group(2)))
        else:
            reqs.append(i)

    return reqs


src = open("pycame/const.py", encoding="utf-8").read()
metadata = dict(re.findall(r'([a-z]+) = "([^"]+)"', src, re.IGNORECASE))
metadata.update(dict(re.findall(r"([a-z]+) = '([^']+)'", src, re.IGNORECASE)))
docstrings = re.findall(r'"""(.*?)"""', src, re.MULTILINE | re.DOTALL)

NAME = "pycame"

PACKAGES = [x for x in find_packages() if x not in ["bin", "tests"]]

VERSION = metadata["VERSION"]
AUTHOR_EMAIL = metadata.get("AUTHOR", "Unknown <no@email.com>")
WEBSITE = metadata.get("WEBSITE", "")
LICENSE = metadata.get("LICENSE", "")
DESCRIPTION = docstrings[0]

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    # "License :: Other/Proprietary License",   # fixme; pylint: disable=fixme
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Home Automation",
]

with open("README.md", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()
    LONG_DESCRIPTION_TYPE = "text/markdown"

# Extract name and e-mail ("Firstname Lastname <mail@example.org>")
AUTHOR, EMAIL = re.match(r"(.*) <(.*)>", AUTHOR_EMAIL).groups()

REQUIREMENTS = load_requirements("requirements.txt")
TEST_REQUIREMENTS = load_requirements("requirements-test.txt")

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    url=WEBSITE,
    packages=PACKAGES,
    install_requires=REQUIREMENTS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_TYPE,
    classifiers=CLASSIFIERS,
    cmdclass={"pytest": PyTest},
    test_suite="tests",
    tests_require=TEST_REQUIREMENTS,
)
