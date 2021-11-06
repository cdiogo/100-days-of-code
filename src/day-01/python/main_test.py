import unittest
from main import convert


class TestConvertToDays(unittest.TestCase):

  def testShouldConvertWithInteger(self):
    """
      Test convert receiving an integer value
    """
    self.assertEqual(convert(10), 3650)

  def testShouldReturnAnException(self):
    """
      Test convert receiving an integer string
    """
    self.assertEqual(convert("oi"), "Please inform a valid number")

if __name__ == "__main__":
  unittest.main()
  print("All tests passed")
