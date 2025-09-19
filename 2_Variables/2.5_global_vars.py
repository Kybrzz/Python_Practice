# global vars can be used both inside nd outside of functions 

## var created outside a function, used inside a function 
x = "Everything is awesome!"
def myfunc():
    print("OYE! " + x)

myfunc() # if this isn't here, the code doesn't execute 

### var created inside function; used inside a function 
y = "Everything is NOT awesome!" 
def myfunc2():
    print("HEY! " + y)

myfunc2() 

#### global keyword = var belongs to a global scope 
def myfunc3():
    global z
    z = "PERFECT!" 
myfunc3()
print("I AM " + z) 

##### global var is alterable in v. out of function 
a = "awesome"

def myfunc4():
    global a
    a = "Purrfection"
myfunc4()
print("THIS is how u do " + a) 