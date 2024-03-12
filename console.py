#!/usr/bin/python3
"""Entry point of the command line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the HBNB class"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit HBNB console """
        exit()

    def do_EOF(self, line):
        """Exit HBNB console """
        return True

    # def do_help(self, line):
    #     """HBNB help documentation"""
    #     self.print_topics()
    #     print(self.complete_help(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
