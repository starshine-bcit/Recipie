import pathlib
from setuptools import setup, find_packages
HERE = pathlib.Path(__file__).parent
VERSION = '1.0.0'
PACKAGE_NAME = 'recipie'
AUTHOR = 'starshine-bcit'
AUTHOR_EMAIL = 'sfey1@my.bcit.ca'
URL = 'https://github.com/SeanXYTan/ACIT2911'
LICENSE = 'GPLv3'
DESCRIPTION = 'A cross-platform Qt recipe database and search program'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = ['PyQt6', 'wheel']
PACKAGE_DIR = {"recipie": "."}

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
      package_dir=PACKAGE_DIR,
      package_data={'recipie': ['data/**/*', 'data/*', 'data/quotes/*', 'image/*', 'LICENSE']},
      include_package_data=True,
      packages=['recipie', 'recipie.modules', 'recipie.data', 'recipie.image']
      )
