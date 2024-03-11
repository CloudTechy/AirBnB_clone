#!/usr/bin/python3
""" This defines a Base_model class"""

import uuid
from datetime import datetime


class BaseModel:
    """ This creatses a representation of a BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ initializes the BaseModel class """
        print(kwargs)
        print()
        if kwargs:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())
                pass
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                        )
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                        )
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Returns the string representation of BaseModel """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """  updates the public instance attribute updated_at with
            the current datetime  """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


# Test the BaseModel class
if __name__ == "__main__":
    # b = BaseModel()
    # print(b.to_dict())
    # b_copy = BaseModel(b.to_dict)

    dict = {
        # 'id': '9626be2c-c964-4453-a1b6-4184f703c298',
        'created_at': '2024-03-11T10:27:00.941821',
        'updated_at': '2024-03-11T10:27:00.941821',
        '__class__': 'BaseModel'
        }
    c = BaseModel(**dict)
    print()
    print(c)
