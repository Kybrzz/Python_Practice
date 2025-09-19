# python allows u to assign multiple values to multiple variables in one line 

a, b, c = "Red", float(2), int(21) 
print(a)
print(b)
print(c) 

## also allowed to assign the same value to multiple vars

x = y = z = "Golden" 
print (x, y, z) # acknowledge the diff between this nd the other 3 lines
print (x)
print(y)
print(z)

### unpacking: collection of values extracted into vars 

fruits = ["Apples", "Blueberries", "Peaches"] 
q, w, e = fruits 
print(q)
print(w)
print(e)