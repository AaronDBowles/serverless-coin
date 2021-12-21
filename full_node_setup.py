from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = [Extension(name="full_node", sources=["src/node.pyx"]),
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
    description='Runs the Full Node',
    ext_modules=cythonize(ext)
)
