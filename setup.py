from setuptools import setup, find_packages


try:
    with open('requirements/base.txt') as req:
        REQUIREMENTS = [r.partition('#')[0] for r in req if not r.startswith('-e')]
except OSError:
    # Shouldn't happen
    REQUIREMENTS = []

with open("README.md", "r") as readme:
    README = readme.read()

# *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
VERSION = '1.0.0'

setup(
    name="gsy-dex",
    description="GSy Decentralized Exchange",
    long_description=README,
    author='GridSingularity',
    author_email='contact@gridsingularity.com',
    url='https://github.com/gridsingularity/gsy-dex',
    version=VERSION,
    packages=find_packages(where=".", exclude=["tests"]),
    package_dir={"gsy_dex": "gsy_dex"},
    package_data={},
    install_requires=REQUIREMENTS,
    zip_safe=False,
)
