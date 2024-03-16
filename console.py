#!/usr/bin/python3
""" Defines HBNB cmd"""

import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl
    
class HBNBCommand(cmd.Cmd):
    """ Represents the HBNB class"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass
    
    def do_quit(self, line):
        """Exit HBNB console """
        return True

    def do_EOF(self, line):
        """Exit HBNB console """
        return True
    
    def do_create(self, line):
        """ Usage: create <class>
        Creates a new instance of BaseModel, saves it and prints the id
        """
        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            pass


    # def do_help(self, line):
    #     """HBNB help documentation"""
    #     self.print_topics()
    #     print(self.complete_help(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
