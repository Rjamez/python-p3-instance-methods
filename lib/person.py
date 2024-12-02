#!/usr/bin/env python3

class Person:
    # Instance method definition
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")


guido = Person()
guido.talk()  # This will call the method and print the message
guido.walk()
    
