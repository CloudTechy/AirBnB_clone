#!/usr/bin/python3
""" Defines File storage class """

import json
from models.base_model import BaseModel
from datetime import datetime


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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):

        """ Serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
        {k: v.to_dict() for k, v in FileStorage.__objects.items()},
        f,
        default=lambda x: x.isoformat() if isinstance(x, datetime) else x
    )

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data_dict = json.load(f)
                for obj_data in data_dict.values():
                    cls_name = obj_data.get("__class__")
                    if cls_name is None:
                        # Handle missing class name
                        continue
                    
                    # Get the class from the class name
                    cls = globals().get(cls_name)
                    # Remove the class name from the object data
                    obj_data.pop("__class__", None)

                    # Create an instance of the class with the object data
                    instance = cls(**obj_data)
                    
                    # Add the instance to the __objects dictionary
                    key = "{}.{}".format(cls.__name__, instance.id)
                    self.__objects[key] = instance
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
