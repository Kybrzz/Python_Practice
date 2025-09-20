# using previous print format, we cannot concatenate strs nd nums by using the '+' operator
## workaround: use the 'f-srings' or 'format()' method
### use f-strings when formatting strings
age = 27
ex1 = f"My name is Bartholemeyou, and I am {age}."
print(ex1)

#### placeholder: a char, word, or str of characters that is a temp. value until a formal value/var is designated
price = 999
txt = f"The price is {price} dollars."
print(txt)

##### placeholders can include a 'modifier' to format the value
# included by adding a colon followed by legal formatting type
txt1 = f"The price is {price:.2f} dollars."  # .2f = fixed-point # w/ 2 decimals
print(txt1)

###### placeholders can also perform math ops.
txt2 = f"The price is {20 * price} dollars."
print(txt2)
