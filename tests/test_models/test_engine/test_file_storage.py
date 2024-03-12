#!/usr/bin/python3
""" Represents unittest for FilStorage model"""

import unittest
import os
from AirBnB_clone.models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Run once before all tests """
        cls.file_path = "file.json"
        bm1 = BaseModel()
        bm2 = BaseModel()
        cls.fs = FileStorage()
        cls.fs.new(bm1)
        cls.fs.new(bm2)
        cls.fs.save()
        cls.test_objects = cls.fs.all()

    @classmethod
    def tearDownClass(cls):
        """ Run once after all tests """
        # Remove the temporary test file
        os.remove(cls.file_path)

    def setUp(self):
        """ Run before each test """
        self.file_storage = self.fs
        # self.file_storage.reload()

    def tearDown(self):
        """ Run after each test """
        # Reset FileStorage to initial state
        # self.file_storage.__objects = {}

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
        new_obj = BaseModel()
        self.file_storage.new(new_obj)

        # Check if object is added
        objects = self.file_storage.all()
        self.assertIn(f"BaseModel.{new_obj.id}", objects)

        # Save objects to file
        self.file_storage.save()

        # Reload objects from file
        self.file_storage.reload()
        objects_after_save = self.file_storage.all()

        # Check if object is still present after saving and reloading
        self.assertIn(f"BaseModel.{new_obj.id}", objects_after_save)
        self.assertEqual(objects_after_save[f"BaseModel.{new_obj.id}"].to_dict(), new_obj.to_dict())
        

    def test_reload(self):
        """ Test the reload() method """
        # Reload should overwrite existing objects with test data
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertEqual(objects, self.test_objects)


if __name__ == '__main__':
    unittest.main()
