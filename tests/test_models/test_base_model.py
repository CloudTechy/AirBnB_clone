#!/usr/bin/python3

"""Defines unittests for base_model.py

"""
import unittest
from models.base_model import Base_model


class TestBaseModel_instantation(unittest.TestCase):
    """ Tests the instantation of Base_model """

    def test_with_no_args(self):
        b1 = Base_model()
        b2 = Base_model()
        self.assertEqual(b1, b2)


if __name__ == "__main__":
    unittest.main()
