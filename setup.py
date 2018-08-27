from setuptools import setup


setup(name="transpopy",
      packages=["transpopy"],
      license="BSD2CLAUSE",
      install_requires=['google-cloud-translate'],
      scripts=['scripts/transpopy'],
      version='0.1.1',
      description='A simple script to translate po files.',
      long_description=("Read a po file and translate the msgids with the "
                        "google translate API."),
      author='Silvio Ap Silva a.k.a Kanazuchi',
      author_email='contato@kanazuchi.com',
      url='http://github.com/kanazux/transpopy',
      zip_safe=False)
