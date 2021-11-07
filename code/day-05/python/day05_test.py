import unittest
from day05 import progress_days

class test_progress_days(unittest.TestCase):

  def test_should_return_2_progress_days(self):
    progress = "3 4 1 2"
    self.assertEqual(progress_days(progress), 2)

  def test_should_return_0_progress_days(self):
    progress= "2 2 2 2"
    self.assertEqual(progress_days(progress), 0)

  def test_should_return_3_progress_days(self):
    progress = "10 11 12 9 10"
    self.assertEqual(progress_days(progress), 3)

  def test_should_return_1_progress_days(self):
    progress = "6 5 4 3 2 9"
    self.assertEqual(progress_days(progress), 1)

if __name__ == "__main__":
  unittest.main(verbosity=2)
