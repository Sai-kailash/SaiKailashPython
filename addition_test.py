import unittest
import pytest
from addition import Addition
from subtract import Subtraction
class Addition_Test_case(unittest.TestCase):
  def test_addition_test_1(self):
    result=Addition.add(1,6)
    #print(result)
    self.assertEqual(result,7)

  def test_subtract_test_1(self):
    result = Subtraction.subtract(5, 1)
    # print(result)
    self.assertEqual(result, 4)







