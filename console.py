#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command line interpreter """
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