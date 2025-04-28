class iterator:

    def __init__(self):
        pass

    def function(self): # blank function to be overwritten
        pass
    
    def loop(self, input): # loop that is general to all iterators - use generalised nested multiloop
        for i in range(input):
            self.function()

class foo(iterator): # foo is an iterator

    def __init__(self):
        super().__init__() # initiates parent class in initiation

    def function(self): # overite of function
        print("hello")

instance = foo() # potential to have each "foo" have unique arguements

instance.loop(5) # run the loop