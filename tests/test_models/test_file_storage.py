#!/usr/bin/python3
""" Represents unittest for FilStorage model"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Run once before all tests """
        cls.file_path = "test_file.json"
        cls.test_objects = {
                "TestClass1.1": {"id": "1", "name": "Test Object 1"},
                "TestClass2.2": {"id": "2", "name": "Test Object 2"}
                }
        # Create a temporary test file with some data
        with open(cls.file_path, 'w') as f:
            json.dump(cls.test_objects, f)

    @classmethod
    def tearDownClass(cls):
        """ Run once after all tests """
        # Remove the temporary test file
        os.remove(cls.file_path)

    def setUp(self):
        """ Run before each test """
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path
        self.file_storage.reload()

    def tearDown(self):
        """ Run after each test """
        # Reset FileStorage to initial state
        self.file_storage.__objects = {}

    def test_all(self):
        """ Test the all() method """
        # Reload should overwrite existing objects with test data
        self.file_storage.reload()
        objects = self.file_storage.all()

        # Check if the number of objects matches the expected test objects
        self.assertEqual(len(objects), len(self.test_objects))

        # Check if each key in test_objects is present in objects
        for key in self.test_objects:
            self.assertIn(key, objects)

        # Check if the values of each key match the expected test data
        for key, value in self.test_objects.items():
            self.assertEqual(objects[key], value)

    def test_new_and_save(self):
        """ Test the new() and save() methods """
        # Create a new object
        new_obj = {"id": "3", "name": "Test Object 3"}
        self.file_storage.new(new_obj)

        # Check if object is added
        objects = self.file_storage.all()
        self.assertIn("TestClass3.3", objects)

        # Save objects to file
        self.file_storage.save()

        # Reload objects from file
        self.file_storage.reload()
        objects_after_save = self.file_storage.all()

        # Check if object is still present after saving and reloading
        self.assertIn("TestClass3.3", objects_after_save)
        self.assertEqual(objects_after_save["TestClass3.3"], new_obj)

    def test_reload(self):
        """ Test the reload() method """
        # Reload should overwrite existing objects with test data
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertEqual(objects, self.test_objects)


if __name__ == '__main__':
    unittest.main()
