"""
Part 1: Discussion 
 
1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Encapsulation, data proximity. Data lives close to its functionality. 
	   With classes and object orientation, we can have data and methods 
	   close to their function and use. 
   
   Abstraction. No need to know the information a method uses internally.
   		We don't need to look at the information the method uses internally
   		to make use of the method itself. It's like the key to a car. 
   		You have the key, car, can drive. We don't need to look at whether
   		it runs on internal combustion, steam or magic. It runs. We drive. 

   The ability to easily make different, interchangeable types of an object. 
   		Imagine you are Noah on the Arc, trying to catalog and track the animals. 
   		Create a super class with main attributes - species, food, habitat, speech, 
   		mammal, etc. Instantiate sub classes - crustacean, bird, dog, cat, horse, etc.
   		The super class acts as a template, a blue print for different types of an
   		object or objects.


2. What is a class?
	A class is like a smarter dictionary. It stores data, is structured, 
	has its own methods / functions and is somewhat flexible.


3. What is an instance attribute?  
	An instance attribute is an attribute set directly on the object or instance.


4. What is a method?
	A method is a function defined on a class.	


5. What is an instance in object orientation?
	An instance is an individual occurrence of a class. It is equivalent to object.


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a piece of data on the class itself. 
   An instance attribute is a piece of data set directly on the instance / object.

   Example: 
   		class Animal(object)
   			legs = 4                     <-- class attribute

   			def __init__(self, name):    
   				self.name = name         <-- instance attributes
   				self.species = species        " "
   			
   		If we instantiate - fido = Animal() - 
   			we can change the species in the instance
   			the change is not reflected in the class. 
   			It is specific to the instance "Fido"

"""

# Parts 2 through 5:
# Create your classes and class methods
"""

Part 2: Class and Init Methods

"""

class Student(object)

	def __init__(self, first_name, last_name):    
		self.first_name = None
		self.last_name = None
		self.address = None

	def __repr__(self):
		return '<%s %s %s>' % (self.first_name, self.last_name, self.address) 


class Question(object)

	def __init__(self):    
		self.question_1 = "What is the capital of Alberta?"
		self.answer_1 = "Edmonton"
		self.question_2 = "Who is the author of Python?"
		self.answer_2 = "Guido Van Rossum"

	def __repr__(self):
		return '<%s: %s >' % (self.question_1, self.answer_1) 
		return '<%s: %s >' % (self.question_2, self.answer_2) 

"""

Part 3 - 5: Not completed

"""