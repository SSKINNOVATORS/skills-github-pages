from setuptools import setup,find_packages

setup(name='morepath_app',
      packages=find_packages(),
      namespace_packages=['morepath_app'],
      install_requires=[
         "morepath>=0.14",
        "more.transaction",
        "zope.sqlalchemy >= 0.7.4",
        "sqlalchemy >= 0.9",
      ],
      entry_points={
         'console_scripts': [
          'morepath_app-start = morepath_app.run:run'
          ]
      })