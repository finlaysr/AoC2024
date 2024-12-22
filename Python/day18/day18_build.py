from setuptools import setup
from Cython.Build import cythonize

setup(
    name='AOC day 18 Part 2',
    ext_modules=cythonize("hello.pyx"),
)