# ints = +/- non-decimal numbers
x = -1
y = 383838
print(x + y)
print(x, y)

## floats = +/- decimals
## can also be scientific notation numbers (e); e indic8s to the power of 10
z = 1.0
a = -5
b = 31e4
print(type(z), type(a))
print(type(z), type(b))

### numeric type conversion
### convert from int to floats
r = float(x)  # x is an int, r is new var, which is now a float
y = float(
    y
)  # ? i believe this makes a new y var, converting prev to current; in this case from int. to float.
#### random is used as a b-i module to generate random numbers w/ in a range
import random  # typically @ top of file

print(random.randrange(1, 100))
