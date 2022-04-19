import unittest
import pytest
from addition import Addition
class Addition_Test_case(unittest.TestCase):
  def test_addition_test_1(self):
    result=Addition.add(1,6)
    #print(result)
    self.assertEqual(result,7)





