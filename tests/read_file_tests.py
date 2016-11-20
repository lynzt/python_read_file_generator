import unittest
from read_file import read_file

class UtilsTests(unittest.TestCase):
    def test_read_file(self):
        data_file = read_file.read_file('/test1')
        print data_file

# python -m unittest discover -s tests -p "*_tests.py"
