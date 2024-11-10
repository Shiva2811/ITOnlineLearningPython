class MyClass:
    class_variable= "I am a class variable"

def __init__ (self, attribute1, attribute2):
    self.attribute1 = attribute1
    self.attribute2 = attribute2

    def instant_method(self):
        return "I am an instance method"
    
    object = MyClass("value1", "value2")

    object.attribute1
    MyClass.class_variable

    object.instant_method()