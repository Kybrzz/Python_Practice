# str data type = str (surrounded by either '_' or "_")
## ex of str data type
### casting/type conversion = the process of converting one data type into another


### notice the disparity in 'em
print(str("Whaddup"))
print("What's up?")
print("'Double' quotation example")

#### assigning a str to a var
ex = "Example String"
print(ex)

##### assigning a multiline str to a var
ex2 = """This
is an example of
a multiline string
assigned to a var"""
print(ex2)

###### array rship (relationship)
"""
- strs in py (python) r arrays of unicode charactes 
- py does not contain a character (char?) data type 
- a single character is a str w/ a length of 1 
- square brackets can b used to access elements of the str
- first char has the position 0 
"""
ex3 = "Used to find position here"
print(ex3[1])

####### strings r arrays, so the chars can b looped using a 'for' loop
for ex3 in "mango":
    print(ex3)
for x in "juxtapose":
    print(x)


######## 'len()' func = obtains length of a str
i = "This gauges ! the _length of a string variable."
print(len(i))

######### 'in' keyword = checks if a particular character of phrase is present ina str
txt = "Let it grow...You greedy dirtbag!"
print("grow" in txt)
# ex. of it used in an 'if' statement
if "grow" in txt:
    print("Claro, 'grow' es presente.")

########## 'not' keyword = checks if a partiuclar char or phrase is NOT present in a str
print("die" not in txt)
## ex. of it used in 'if' statement
if "die" not in txt:
    print("Error. 'Die' no es presente en eso txt")
