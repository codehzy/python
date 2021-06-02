import unittest
from name_function import get_formatted


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatter_name = get_formatted('jan', 'joplin')
        self.assertEqual(formatter_name, 'Jan Joplin')


unittest.main()
