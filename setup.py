import pathlib
from setuptools import setup, find_packages
HERE = pathlib.Path(__file__).parent
VERSION = '0.2.2'
PACKAGE_NAME = 'recipie'
AUTHOR = 'starshine-bcit'
AUTHOR_EMAIL = 'sfey1@my.bcit.ca'
URL = 'https://github.com/SeanXYTan/ACIT2911'
LICENSE = 'GPLv3'
DESCRIPTION = 'A cross-platform Qt recipe database and search program'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = ['PyQt6']

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )