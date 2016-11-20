from setuptools import setup, find_packages

print find_packages()
setup(name='python_fec_parse',
      version='0.0.1',
      description='parse fec files',
      author='lynzt',
      url='https://github.com/lynzt/python_fec_parse',
      packages=['fec_parse'],
     )
