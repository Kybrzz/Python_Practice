# operators = symbols/keywords that applies a process to 1 or more operands, producing a result

# operator precedence (top is paramount, descending)
"""
1. parenthesis
2. exponentiation
3. unary plus, unary minus, nd bitwise NOT
4. mult, div, floor div, nd modulus
5. add, sub
6. bitwise left nd right shifts
7. bitwise AND
8. bitwise XOR
9. bitwise OR
10. comparisons, identity, nd membership operators
11. logical NOT
12. AND
13. OR
"""

## list of py arithmetic operators
# used w/ numeric values to compute rudimental mathematical processes
"""
+: addition
-: subtraction
*: multiplication
/: division
%: modulus
**: exponentiation
//: flor division
"""

### list of py assignment operators
# used to assign values to vars
"""
=: equals ao (assignment operator)
+=: addition ao
-=: subtraction ao
*=: multiplication ao
/=: division ao
%=: modulus ao
**=: exponentiation ao
//=: floor division ao
&=: bitwise AND ao
|=: bitwise OR ao 
^=: bitwise XOR ao
>>=: bitwise right shift ao 
<<=: bitwise left shift ao
:=: walrus operator -> used to assign a value to a var within an expression
"""

#### list of py comparison operators
# used to compare two values
"""
==: equals 
!=: DNE
>: greater than
<: less than 
>=: greater than or eq to 
<=: less than or eq to 
"""

##### list of py logical operators
# used to combine conditional statements
"""
and: returns 'True' if both statements r true 
or: returns 'True' if one of the statements is true 
not: inverse the result; returns 'False' if the result is ture 
"""

###### list of py identify operators
# used to compare the same object w/ the same memory locality
"""
is: returns 'True' if both vars r the same object
is not: returns 'True' if both vars r not the same obj 
"""

######## list of py membership operators
# used to test if a sequence is presented in an object
"""
in: returns a 'True' if a sequence w/ the specified value is present in the object
not in: returns 'True' if a sequence w/ the specified value is not present in the object 
"""

######### list of py bitwise operators
# used to compare binary numbers
"""
&: (name) + (description) -> AND; sets each bit to 1 if both bits r 1
|: OR; sets each bit to 1 if one of the two bits is 1
^: XOR; sets each bit to 1 if only one of the two bits is 1
~: NOT; inverts all the bits 
<<: zero fill left shift; shift left by pushing zeroes in from the right nd let the leftmost bits fall off
>>: signed right shift; shift right by pushing copies of the leftmost bit in from the left, letting the rightmost bits fall off
"""
