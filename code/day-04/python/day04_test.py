import unittest

from day04 import skewers_identificator

class test_skewers_identificator(unittest.TestCase):

  def test_should_find_3_veggies_2_non_veggies(self):
    skewers="--oooo-ooo-- --xxxxxxxx-- --o--- -o-----o---x-- --o---o-----"
    self.assertEqual(skewers_identificator(skewers), [3, 2])

  def test_should_find_4_veggies_and_0_non_veggies(self):
    skewers="--oooo-ooo-- -----o- --o--- -o-----o---o--"
    self.assertEqual(skewers_identificator(skewers), [4,0])


if __name__ == "__main__":
  unittest.main(verbosity=2)
