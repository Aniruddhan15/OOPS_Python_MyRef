#Polymorphism

# Python program to demonstrate 
# Defining parent class 
class Parent(): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Parent"
		
	# Parent's show method 
	def show(self): 
		print(self.value) 
		
# Defining child class 
class Child(Parent): 
	
	# Constructor 
	def __init__(self): 
		super().__init__()  # Call parent constructor
		self.value = "Inside Child"
		
	# Child's show method 
	def show(self): 
		print(self.value) 
		
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show()  # Should print "Inside Parent"
obj2.show()  # Should print "Inside Child"


#ex2
# Python program to demonstrate 
# Defining parent class 1 
class Parent1(): 
		
	# Parent's show method 
	def show(self): 
		print("Inside Parent1") 
		
# Defining Parent class 2 
class Parent2(): 
		
	# Parent's show method 
	def display(self): 
		print("Inside Parent2") 
		
		
# Defining child class 
class Child(Parent1, Parent2): 
		
	# Child's show method 
	def show(self): 
		print("Inside Child") 
	
		
# Driver's code 
obj = Child() 

obj.show() 
obj.display()

#ex3
# Python program to demonstrate 
# Python program to demonstrate 
# overriding in multilevel inheritance 

class Parent(): 
		
	# Parent's show method 
	def display(self): 
		print("Inside Parent") 
	
	
# Inherited or Sub class (Note Parent in bracket) 
class Child(Parent): 
		
	# Child's show method 
	def show(self): 
		print("Inside Child") 
	
# Inherited or Sub class (Note Child in bracket) 
class GrandChild(Child): 
		
	# Child's show method 
	def show(self): 
		print("Inside GrandChild")		 
	
# Driver code 
g = GrandChild() 
g.show() 
g.display()

#ex4
# Python program to demonstrate 
# calling the parent's class method 
# inside the overridden method using 
# super() 
class Parent(): 
	
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 
	
	def show(self): 
		
		# Calling the parent's class 
		# method 
		super().show() 
		print("Inside Child") 
		
# Driver's code 
obj = Child() 
obj.show()

#ex5
# Program to define the use of super() 
# function in multiple inheritance 
class GFG1: 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG1)') 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG1:', b) 
	
# class GFG2 inherits the GFG1 
class GFG2(GFG1): 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG2)') 
		super().__init__() 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG2:', b) 
		super().sub_GFG(b + 1) 
	
# class GFG3 inherits the GFG1 ang GFG2 both 
class GFG3(GFG2): 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG3)') 
		super().__init__() 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG3:', b) 
		super().sub_GFG(b + 1) 
	
	
# main function 
if __name__ == '__main__': 
	
	# created the object gfg 
	gfg = GFG3() 
	
	# calling the function sub_GFG3() from class GHG3 
	# which inherits both GFG1 and GFG2 classes 
	gfg.sub_GFG(10)
