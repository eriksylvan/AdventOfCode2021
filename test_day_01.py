import unittest
import day_01

class TestDay01(unittest.TestCase):
    
    def test_day01(self):
        self.assertEqual(day_01.dummy(1), 2)
        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_01_test.py 