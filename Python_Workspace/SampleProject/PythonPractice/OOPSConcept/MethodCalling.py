class AClass():
    """In Python, a class may have several types of methods:
    instance methods, class methods, and static methods
    """
    def an_instance_method(self, fName, lName, age):
        """this is a function of the instance of the object
        self is the object's instance
        """
        age = str(age)
        print(fName + " "+lName + ", age {} is in Instance Method.".format(age))

    @classmethod
    def a_class_method(cls,fName,lName,age):
        """this is a function of the class of the object
        cls is the object's class
        """
        print(fName + " "+lName + ', age '+ age +" is in Class Method.")

    @staticmethod
    def a_static_method(fName,lName,age):
        """this is neither a function of the instance or class to
        which it is attached
        """
        print(fName + " " + lName + ', age ' + age + " is in Static Method.")

# Calling of methods with the help of instance variable of the class.
# Creating instance variable of the class.
instance = AClass()

instance.an_instance_method('Ashish','Srivastava',27)
instance.a_class_method('Ashish','Srivastava','27')
instance.a_static_method('Ashish','Srivastava',str(27))

# Calling of methods with the help of Class name.
AClass.a_class_method('Ashish','Srivastava','27')
AClass.a_static_method('Ashish','Srivastava',str(27))
#AClass.an_instancemethod('Ashish','Srivastava',27)
# Instance method can not be called with the help of Class name.
# To call instance method through class, explicitly we have to pass instance variable of the class.
AClass.an_instance_method(instance,'Ashish','Srivastava',27)