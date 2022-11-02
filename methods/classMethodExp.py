class Testing:
    def __init__(self, name1, name2, name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
    """ 
    It can modify a class state that would apply across all the instances of the class.
    for example, it can modify a class variable that would be applicable to all the instances. 
    """
    @classmethod
    def add(cls, num2, num3):
        return cls(num3, num2, num3 + num2)
    """
    A static method can't access or modify the class properties,
    In general, static methods know nothing about the class state.
    """
    @staticmethod
    def junk(garbage):
        print(garbage)

    """
    If we use instance variables inside a method, such methods are called instance methods,
    A instance method is bound to the object of the class.
    It can access or modify the object state by changing the value of a instance variables
    """
    def disp(self):
        print(f"num1: {self.name1}\nnum2: {self.name2}\nnum3: {self.name3}")


pers = Testing('afnan', 'felix', 'empty')
pers.disp()
print("After Changing the variables")
per = Testing.add('afnan', 'felix')
per.disp()

pers.junk('im a waste fellow')
