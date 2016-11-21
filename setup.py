from setuptools import setup, find_packages

print find_packages()
setup(name='python_read_file',
      version='0.0.1',
      description='read a file | convert list values to dict',
      author='lynzt',
      url='https://github.com/lynzt/python_read_file',
      packages=['read_file'],
      install_requires=[
          'csv',
      ],
     )
