import unittest

from day06 import find_sock_pairs

class test_find_sock_pairs(unittest.TestCase):

  def test_should_find_1_pair(self):
    self.assertEqual(find_sock_pairs("AA"),1)

  def test_should_not_find_any_pair(self):
    self.assertEqual(find_sock_pairs(""),0)

  def test_should_find_2_pairs(self):
    self.assertEqual(find_sock_pairs("CCCC"),2)


if __name__ == "__main__":
  unittest.main(verbosity=2)
