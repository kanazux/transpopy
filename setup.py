from setuptools import setup


setup(name='transpopy',
      version='0.2.0',
      license='BSD2CLAUSE',
      install_requires=['google-cloud-translate'],
      packages=['transpopy'],
      package_data={'transpopy': ['transpopy/*']},
      data_files=[('LICENSE')],
      entry_points={'console_scripts': ['transpopy=transpopy.__main__:main']},
      description='A simple script to translate po files.',
      long_description=("Read a po file and translate the msgids with the "
                        "google translate API."),
      author='Silvio Ap Silva a.k.a Kanazuchi',
      author_email='contato@kanazuchi.com',
      url='http://github.com/kanazux/transpopy',
      zip_safe=False)
