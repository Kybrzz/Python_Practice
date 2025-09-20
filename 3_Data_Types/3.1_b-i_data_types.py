"""
- data types in programming = define the type of value a var contains
- built-in (b-i) data types by default categories, filtered a-h
    a) text type = str
    b) numeric type = int, float, complex
    c) sequence type = list, tuple, range
    d) mapping type = dict
    e) set types = set, frozenset
    f) boolean type = bool
    g) binary type = bytes, bytearray, memoryview
    h) none type = NoneType
- u can obtain the data type but coding the 'type()' function
"""

# text data type
a = str("fyaa")
print(type(a))

## numeric data type
b1 = int(62)
b2 = float(96)
b3 = complex(700)
print(
    type(b1)
)  # acknowledge that u cannot print, using ,'s, on the same line, vars of diff types
print(type(b2))
print(type(b3))

### sequence data type
c1 = list(
    ("items", "in", "list")
)  # edit acknowledgement: w/o specifying data type, list use []; also autocorrects this
c2 = tuple("items", "in", "a", "tuple")
c3 = range(9)
print(type(c1))
print(type(c2))
print(type(c3))

#### mapping data type
d = dict(
    name="John", age=80
)  ## edit ack: w/o specifying data type, dicts use {}, :, and ,
print(type(d))

##### set data types
e1 = set(
    ("same", "ilk", "of", "items")
)  ### edit ack: w/o specifying data type, sets use {}
e2 = frozenset({"this", "is", "frozenset"})
print(type(e1))
print(type(e2))

###### boolean types
f = bool(True)
print(type(f))

####### binary data types
g1 = bytes(b"bytes_type")
g2 = bytearray(2)
g3 = memoryview(bytes(55))
print(type(g1))
print(type(g2))
print(type(g3))

######## none data type
h = None
