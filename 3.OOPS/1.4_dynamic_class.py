'''
dynamic class can be created using the "type" in python

You can also call type() with three arguments—type(<name>, <bases>, <dct>):

<name> specifies the class name. This becomes the __name__ attribute of the class.
<bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.
<dct> specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.

'''

def init(self,name):
    self.name = name

def get_name(self):
    return self.name

Obj = type('Obj', (object,),
           {
               '__init__': init,
               'get_name': get_name,
           })

obj = Obj(name="india")
print(obj.get_name())