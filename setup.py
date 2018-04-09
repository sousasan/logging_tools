from setuptools import setup

setup(name='logging_tools',
      version='0.2',
      description='Tools for logging',
      url='http://github.com/sousasan/logging_tools',
      author='Data Team',
      author_email='data@quandl.com',
      packages=['logging_tools','db_connections'],
      install_requires=['pandas','logging'],
      zip_safe=False)