import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal, Slot

# Define the struct class
class MyStruct:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Communicate(QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    speak = Signal((int,), (str,), (float,), (MyStruct,))

    def __init__(self, parent=None):
        super().__init__(parent)

        self.speak[int].connect(self.say_something)
        self.speak[str].connect(self.say_something)
        self.speak[float].connect(self.say_something)
        self.speak[MyStruct].connect(self.say_something)

    # define a new slot that receives a C 'int' or a 'str' or 'float'
    # and has 'say_something' as its name
    @Slot(int)
    @Slot(str)
    @Slot(float)
    @Slot(MyStruct)
    def say_something(self, arg):
        if isinstance(arg, int):
            print("This is a number:", arg)
        elif isinstance(arg, str):
            print("This is a string:", arg)
        elif isinstance(arg, float):
            print("This is a float:", arg)
        elif isinstance(arg, MyStruct):
            print("This is a struct:", arg.name, arg.value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    someone = Communicate()

    # emit 'speak' signal with different arguments.
    # we have to specify the str as int is the default
    someone.speak[int].emit(10)
    someone.speak[str].emit("Hello everybody!")
    someone.speak[float].emit(10.5**5)
    someone.speak[str].emit("Hello Andrea!")
    someone.speak[MyStruct].emit(MyStruct("Colin", 15))
