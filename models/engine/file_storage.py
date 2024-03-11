#!/usr/bin/python3
""" Defines File storage class """

import json
from models.base_model import BaseModel


class FileStorage:
    """ Serializes instances to a JSON file and
    deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.get("id"))
        FileStorage.__objects[key] = obj

    def save(self):

        """ Serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                    {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                    f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data_dict = json.load(f)
                for obj in data_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass


# if __name__ == "__main__":
#     f = FileStorage()
#     new_obj = {"BaseModel.3": BaseModel().to_dict()}
#     f.new(new_obj)

#     # # Check if object is added
#     # objects = f.all()
#     # print(objects)

#     # # Save objects to file
#     # f.save()

#     # # Reload objects from file
#     # f.reload()
#     objects_after_save = f.all()
#     print(objects_after_save)
