import unittest
from read_file_generator import read_file_generator

class UtilsTests(unittest.TestCase):
    def test_get_data(self):
        count = 0
        for row in read_file_generator.get_data('tests/data/test1.csv', '|'):
            self.assertEqual(len(row), 3)
            if count == 1:
                self.assertEqual(row[0], '1')
                self.assertEqual(row[1], 'hudson')
                self.assertEqual(row[2], 'dog')
                break
            count+=1

        count = 0
        for row in read_file_generator.get_data('tests/data/test2.csv', ','):
            self.assertEqual(len(row), 3)
            if count == 1:
                self.assertEqual(row[0], '1')
                self.assertEqual(row[1], 'hudson')
                self.assertEqual(row[2], 'dog')
                break
            count+=1

    def test_dict_from_list(self):
        rows = read_file_generator.get_data('tests/data/test1.csv', '|')
        count = 0
        for row in rows:
            data = read_file_generator.create_dict_from_list(row, ['id', 'name', 'value'])
            if count == 1:
                self.assertEqual(data['id'], '1')
                self.assertEqual(data['name'], 'hudson')
                self.assertEqual(data['value'], 'dog')
                break
            count+=1

# python -m unittest discover -s tests -p "*_tests.py"
