#!/usr/bin/python3

"""Defines unittests for base_model.py

"""
import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test the initialization of BaseModel."""
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.id, str))
        self.assertTrue(isinstance(base_model.created_at, datetime))
        self.assertTrue(isinstance(base_model.updated_at, datetime))

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            base_model.id,
            base_model.__dict__
        )
        self.assertEqual(str(base_model), expected_str)

    @patch('models.base_model.datetime')
    def test_save(self, mock_datetime):
        """Test the save method of BaseModel."""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        mock_datetime.now.return_value = datetime(2022, 1, 1, 12, 0, 0)
        base_model.save()
        self.assertNotEqual(base_model.updated_at, initial_updated_at)
        self.assertEqual(base_model.updated_at, datetime(2022, 1, 1, 12, 0, 0))

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        expected_dict = {
            '__class__': 'BaseModel',
            'id': base_model.id,
            'created_at': base_model.created_at.isoformat(),
            'updated_at': base_model.updated_at.isoformat()
        }
        self.assertEqual(base_model_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
