
""" Mistake"""
# class Controltower:
#     def __init__(self): instance method , initialize the object
#         print("Initializing Control Tower!")
        

# tower1=Controltower()
# tower2=Controltower()

# print(tower1==tower2) # dicfferent objest are getting created


""" Correction """

class Controltower:
    _instance=None

    def __new__(cls): # __new__ is a static method ,  creates the object
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            print("Initializing Control Tower!")
        return cls._instance

    
tower1=Controltower()
tower2=Controltower()

print(tower1==tower2) # different objest are getting created




# Feature	__new__	                        __init__
# Type	    Static method	              Instance method
# Role	     Creates the object	           Initializes the object
# First         Argument cls (the class)   self (the instance)
# Return Value	Must return an instance	    Must return None
# Call Sequence	Called first	        Called after __new__
