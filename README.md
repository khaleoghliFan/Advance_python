#list:
1- fullname.py
# Advance_python
classes in python
- [source 1](https://colab.research.google.com/drive/1-6uzkDDuUyRjG_a7LZVZdTBxvnZQLBIb#scrollTo=_mXwOPPnCJiY&line=18&uniqifier=1)
- [source 2](https://www.youtube.com/watch?v=iZZtEJjQLjQ&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=2)
## **why do we create classes?**
1-  To create our own custom objects and data types
2-  To define the behavior of objects
3-   For organization and structure

## **different between __ str __ and __ repr __:**

The __str__ method essentially defines what happens when you typecast the vector into a string. This method is intended to provide a human-readable or informal string representation of an object

The __repr__ method essentially tells Python how to represent a vector when we need to represent it. This representation is often more geared towards developers and should ideally be unambiguous and potentially used to recreate the object

## **__ call __: ** you can then call that object using parentheses, just like you would call a regular function.


## **__self__:**

Automatic First Argument: When you define a method inside a class, the first parameter it takes is, by convention, named self. Python automatically passes the instance of the class as this first argument when you call the method on an object.


Reference to the Instance: The self parameter acts as a reference to the specific object that the method is associated with. Think of it as the method saying, "I am operating on this particular employee" when you call a method on an Employee object.


Accessing Instance Attributes: Inside a method, you use self followed by a dot (.) to access the instance variables (attributes) of that object. For example, in the __init__ method, self.first = first assigns the value of the first argument to the first attribute of the specific Employee instance being created. Similarly, in the full_name method, self.first and self.last refer to the first and last names of the particular employee whose full name is being requested.


Calling Other Methods: Within a method, you can also use self to call other methods belonging to the same instance.


Initialization (__init__): The __init__ method, which is the constructor of the class, always takes self as its first parameter. This is where you typically initialize the instance variables of the object using the self reference. When you create a new instance of a class (e.g., employee1 = Employee(...)), Python automatically calls the __init__ method and passes the newly created object as the self argument.


Method Invocation: When you call a method on an instance (e.g., employee1.full_name()), you don't explicitly pass any argument for self. Python handles this automatically, passing employee1 as the self argument to the full_name method.


Calling Methods on the Class: You can also call a method directly on the class itself (e.g., Employee.full_name(employee1)). In this case, you must explicitly pass the instance (employee1) as the argument, and within the full_name method, this argument will be received as self. This illustrates the underlying mechanism of how instance methods are associated with specific objects.


Convention, Not Keyword: While self is a strong convention and highly recommended, it's technically not a reserved keyword in Python. However, you should always stick to using self as the first parameter in instance methods for clarity and to adhere to Python best practices. Forgetting to include self will lead to a TypeError when you try to call the method on an object, as Python will expect an instance to be passed.


In essence, self is the glue that connects a method to the specific instance of the class it is operating on, allowing the method to access and modify the instance's attributes and call its other methods.

## **Class variable**
 class variables are variables that are** shared among all instances of a class**. This is in contrast to instance variables, which hold data that is unique to each individual instance of the class.
Here's a more detailed explanation of class variables:
Shared Data: The primary characteristic of a class variable is that its value is the same for every object (instance) created from that class. The transcript provides an example of a company's annual raise percentage. This raise amount would typically be the same for all employees, making it a good candidate for a class variable.


* Declaration: Class variables are defined within the class definition but outside of any instance methods (like the __init__ method). The transcript shows an example where raise_amount = 1.04 is defined at the top of the Employee class.


* Accessing Class Variables:
You can access class variables using the class name itself (e.g., Employee.raise_amount).
You can also access them through an instance of the class (e.g., employee1.raise_amount).
When you try to access an attribute on an instance, Python first checks if the instance has that attribute. If it doesn't, it then looks in the class and any classes it inherits from. Therefore, when you access raise_amount from an instance that doesn't have its own raise_amount attribute, you are actually accessing the class's raise_amount attribute.


* Use Cases:
Constants shared across all instances: As in the raise amount example, class variables are useful for values that should be consistent across all objects of a class.
Tracking class-level information: The transcript introduces another example of num_of_employees. This variable keeps track of the total number of Employee instances created. Since this count should be the same regardless of the specific employee instance, it is implemented as a class variable that is incremented in the __init__ method (which runs every time a new employee is created). The transcript explicitly states that using Employee.num_of_employees is preferred here because there's no logical reason for the total number of employees to be different for any single employee instance.




* Modifying Class Variables:
Modifying through the class: If you modify a class variable using the class name (e.g., Employee.raise_amount = 1.05), the change will be reflected for the class itself and all existing instances that haven't overridden the class variable at the instance level.


Modifying through an instance: If you assign a new value to a class variable using an instance (e.g., employee1.raise_amount = 1.05), it does not change the class variable for other instances or the class itself. Instead, it creates a new instance attribute with the same name for that specific instance. When you subsequently access employee1.raise_amount, you will retrieve the instance-specific value. Other instances will still access the class's raise_amount value. You can observe this by printing the namespace (__dict__) of the instance, which will now include the newly assigned attribute.


* Accessing within Methods (self vs. Class Name):
Within instance methods, you can access class variables using either self.raise_amount or Employee.raise_amount.

The transcript suggests using self.raise_amount in the apply_raise method. This allows for the possibility of an individual instance having a different raise amount if needed. If a subclass is created, using self will also allow the subclass to potentially override the raise amount.
However, for class variables like num_of_employees, where the value should truly be shared and not overridden per instance, the transcript recommends using the class name (Employee.num_of_employees) to ensure that the class-level variable is being accessed and modified.




