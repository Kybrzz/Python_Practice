# 'slice' syntax = returns a range of characters from specified positions
# includes first number, stops @ second number
ex = "Sliced example"
print(ex[2:8])

## slicing from the start = range begins w/ first character
ex2 = "Start-slice example"
print(ex2[:5])

### slicing to the end = range goes to the end
ex3 = "End-slice example"
print(ex3[3:])

#### negative indexing = begin the slice from the end of the string
ex4 = "negative-indexing example"
print(ex4[-8:-5])
