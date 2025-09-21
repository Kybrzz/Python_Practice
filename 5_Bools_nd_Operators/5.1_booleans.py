# boolean def: a type of algabreic login in which results r calculated as either false (represented w/ 0), or true (any nonzero #)
## the 'bool' func allows u to evalu8 any value, returning a bool result
print(bool("test bool"))
print(bool(15))


### acknowledge how nearly all arguments r evalu8ed as true
#### funtions can return bool values
def test_function():
    return False


print(test_function())


##### ex. of using an if-else statement w/ a bool
def test2_function():
    return True


if test2_function():
    print(f"Correcto!")
else:
    print(f"No")

### 'isinstance()' func: determines if an object is a particular data type
a = 200
print(isinstance(a, int))
