from setuptools import setup, find_packages

setup(
    name="advent-of-code-2020",
    version="0.1",
    description="Ted's solutions for https://adventofcode.com/",
    url="https://github.com/TedCassirer/advent-of-code-2020",
    author="Ted Cassirer",
    author_email="ted.cassirer@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.8.0",
        "black >= 23.1a1",
        "numpy >= 1.19.4",
        "pytest >= 6.1.2",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["cas = aoc_cas:solve"],
        "console_scripts": ["aoccas = aoc_cas.cli:main"],
    },
)
