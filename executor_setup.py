from setuptools import setup, Extension
from Cython.Build import cythonize

ext = [Extension(name="executor", sources=["src/executor.pyx"]),
       Extension(name="*", sources=["src/core/*.pyx"]),
       Extension(name="*", sources=["src/core/primitives/*.pyx"])]
setup(
    name='serverless-coin',
    version='0',
    packages=[''],
    url='',
    license='',
    author='Aaron Bowles',
    author_email='Bowles.Aarond@gmail.com',
    description='Runs the Executor Node',
    ext_modules=cythonize(ext)
)
