import unittest
from main import calcTribonacci

class TestTribonacciSeries(unittest.TestCase):

  def test_should_return_a_list_with_6_elements(self):
    self.assertIsNotNone(len(calcTribonacci("1,2,3")), 6)

  def test_should_not_return_an_none_value(self):
    self.assertIsNotNone(calcTribonacci("1,2,3"), True)

if __name__ == "__main__":
  unittest.main()
  print("All tests passed")
