from setuptools import setup, find_packages
import os

# hack for working with pandocs on windows
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    utf8 = codecs.lookup('utf-8')
    func = lambda name, enc=utf8: {True: enc}.get(name == 'mbcs')
    codecs.register(func)

# install readme
README = os.path.join(os.path.dirname(__file__), 'README.md')

try:
    long_description = open(README).read()
except:
    long_description = ""

REQUIREMENTS = os.path.join(os.path.dirname(__file__), 'requirements.txt')
REQUIREMENTS = open(REQUIREMENTS, 'r').read().splitlines()

VERSION = os.path.join(os.path.dirname(__file__), 'VERSION')
VERSION = open(VERSION, 'r').read().strip()

# setup
setup(
    name='ableton',
    version=VERSION,
    description='Create and Manage Ableton files in Python.',
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Brian Abelson',
    author_email='brianabelson@gmail.com',
    url='http://github.com/abelsonlive/ableton',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    tests_require=[]
)
