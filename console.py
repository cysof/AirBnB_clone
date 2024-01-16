#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    #list of all class

    CLASS_MAP = {"BaseModel": BaseModel, "User": User,
            "State": State, "City": City, "Place": Place,
            "Amenity": Amenity, "Review": Review}

    def do_quit(self, arg):
        """
        Quit command to exit the program

        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when the end-of-file (EOF) character is encountered
        """

        return True

    def emptyline(self):
        """
        do nothing when empty line + ENTER

        """
        pass

    def do_create(self, arg):
        """
        Usage: Create <class_name>
        This create new instance of BaseModel, save it and print the id.

        """
        if not arg:
            print(" **class name missing ** ")
            return
        if arg in HBNBCommand.CLASS_MAP:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")


    def do_show(self, arg):
        """Print the string representation of an instance
        Usage: show BaseModel 1234-1234-1234
        """

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()

        if args[0] not in HBNBCommand.CLASS_MAP:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

        def do_destroy(self, arg):
            """Delete an instance based on class name and id.
            Usage: destroy BaseModel 1234-1234-1234
            """

            if not arg:
                print("** class name missing **")
                return

            args = arg.split()
            if args[0] not in HBNBCommand.CLASS_MAP:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                objects.pop(key)
                storage.save()
            else:
                print("** no instance found **")

            def do_all(self, arg):
                """Print all string representations of instances
                Usage: all Basemodel or all
                """
                args = arg.split()
                objects = storage.all()

                if len(args) == 0:
                    print([str(obj) for obj in objects.values()])
                elif len(args) == 1 and args[0] in HBNBCommand.CLASS_MAP:
                    print([str(obj) for obj in objects.values() 
                        if type(obj).__name__ == args[0]])
                else:
                    print("** class doesn't exist **")

            def do_update(self, arg):
                """Update an instance attribute based on classname and id
                Usage: update <class> <id> <attribute name> <attribute value>
                """
                if not arg:
                    print("** class name missing **")

                args = arg.split()

                if args[0] not in HBNBCommand.CLASS_MAP:
                    print("** class doesn't exist **")
                    return

                if len(args) < 2:
                    print("** instance id missing **")
                    return

                objects = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key not in objects:
                    print("** no instance found **")
                    return
                if len(args) < 3:
                    print("** no instance found **")
                    return

                if len(args) < 4:
                    print("** attribute name missing **")

                if len(args) == 4:
                    obj = objects[key]
                    attribute_name = args[2]
                    #Removing leading trailing whitespaces / quotes
                    attribute_value = args[3].strip("'\"")
                    if hasattr(obj, attribute_name):
                        setattr(obj, attribute_name, attribute_value)
                        obj.save()
                    else:
                        print("** attribute doesn't exist **")









if __name__ == '__main__':
    HBNBCommand().cmdloop()
