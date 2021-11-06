import unittest
from day03 import find_nemo

class test_find_nemo(unittest.TestCase):

  def test_if_multiple_nemos_return_firs_one(self):
    self.assertEqual(find_nemo("My name is Nemo and Nemo"), "I found Nemo at 4")

  def test_if_find_nemo_correctly(self):
    self.assertEqual(find_nemo("Hi Nemo"), "I found Nemo at 2")

  def test_if_nemo_word_is_with_something(self):
    self.assertEqual(find_nemo("It's Nemo's pencil"), "I can't find Nemo :(")

  def test_if_dont_find_nemo_with_variations(self):
    self.assertEqual(find_nemo("Hi nemo"), "I can't find Nemo :(")
if __name__ == "__main__":
  unittest.main(verbosity=2)
