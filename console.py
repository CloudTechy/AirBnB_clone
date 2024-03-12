#!/usr/bin/python3
""" Defines HBNB cmd"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Represents the HBNB class"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass
    
    def do_quit(self, arg):
        """Exit HBNB console """
        return True

    def do_EOF(self, arg):
        """Exit HBNB console """
        return True

    # def do_help(self, line):
    #     """HBNB help documentation"""
    #     self.print_topics()
    #     print(self.complete_help(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
