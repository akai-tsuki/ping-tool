# -*- coding: utf-8 -*-

import unittest
import nose
import sample

class TestSample(unittest.TestCase):
  
  def test_hello(self):
    self.assertEqual(sample.hello(), "hello")

if __name__ == '__main__':
  unittest.main()
