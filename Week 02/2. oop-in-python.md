# Object-Oriented Programming in Python

Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects. Python is an object oriented programming language. 

## Classes and Objects

* A **`class`** is like an object constructor, or a "blueprint" for creating objects. A class is a collection of objects. 
* An **`object`** is an entity that has a state and behavior associated with it. Almost everything in Python is an object, with its properties and methods. Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects. More specifically, any single integer or any single string is an object.
* An object consists of:
  - `State` - attributes of an object which reflect the properties of an object
  - `Behavior` - methods of an object which reflect the response of an object to other objects
  - `Identity` - a unique name given to an object which enable one object to interact with other objects

```python
class Customer:
    def __init__(self,name,membership):
        self.name = name
        self.membership = membership
        print(" Valued Customer: ")

c = Customer('Taimur', 'Platinum')
print(c.name,c.membership)
```

We can create a list of objects as follows:

```python
customers = [Customer('Taimur', 'Platinum'), Customer('Ibrahim', 'Gold')]

```

## What is `self` in Class?
`Class` methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it. If we have a method that takes no arguments, then we still have to have one argument. When we call a method of an object as `myobject.method(arg1, arg2)`, this is automatically converted by Python into `MyClass.method(myobject, arg1, arg2)` – this is all the special self is about.

## What is the `__init__` Method?
It is the default constructor in C++ and Java. Constructors are used to initializing the object’s state. The task of constructors is to initialize the data members of the class when an object of the class is created. Like methods, a constructor also contains a collection of statements that are executed at the time of object creation. It is run as soon as an object of a class is instantiated.

```python
class Person:
	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Zain')
p.say_hi()
```

## Creaton of Classes and Objects

```python
class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("Customer created")
    def update_membership(self, new_membership):
        print("Calculating costs")
        self.membership_type = new_membership
    def __str__(self):
        return self.name + ' ' + self.membership_type
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False
```

```python
customers = [Customer('Taimur', 'Platinum'), Customer('Ibrahim', 'Gold')]
print(customers[0].name)
Customer.print_all_customers(customers)
print(customers[0] == customers[1])
```

## What is the `__hash__` Method?
Python hash() function is a built-in function and returns the hash value of an object if it has one. The hash value is an integer which is used to quickly compare dictionary keys while looking at a dictionary. Objects hashed using hash() are irreversible, leading to loss of information. `hash()` returns hashed value only for immutable objects, hence can be used as an indicator to check for mutable/immutable objects.

## OOP Principles

* `Encapsulation`is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables. A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.
* `Inheritance` is the capability of one class to derive or inherit the properties from another class. The benefits of inheritance are:
	- It represents real-world relationships well.
	- It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
	- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A
* `Polymorphism` ets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class does not quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as *method overriding*.

```python
class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I m a teacher")

class Customer(User):
    def __init__(self,name,membership_type):
        self.name = name
        self.membership_type = membership_type

        @property
        def name(self):                       # Getter function
            print("Getting name")
            return self._name

        @name.setter
        def name(self,name):                  # Setter function
            print("Setting name")
            self._name = name

    def update_membership(self,new_membership):
        self.membership_type = new_membership

    def __str__(self):
        return self.name + ' ' + self.membership_type

    def print_all_customers(self):
        for customers in customer:
           print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return  True

        return  False

    __hash__ = None
    __repr__ = __str__
    
users = [Customer('Taimur', 'Platinum'), Customer('Ibrahim', 'Gold')]
for user in users:
    user.log()
```
