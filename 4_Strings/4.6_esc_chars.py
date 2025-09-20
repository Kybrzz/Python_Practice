# escape character uses: to insert characters illegal in a str
## escape character = '\' -> character u want to insert
print(
    f'This is the "typical" way to represent double quotes in a quoted sentence.'
)  # squiggly line bc this is claimed to be 'unnecessary' if there r no expressions to format

print(f'Using a newline, u can "bypass" this rule.')

### other escape chars used in python;
"""
\' = single quote 
\\ = backslash 
\n = new line 
\r carriage return 
\t = tab 
\b = backspace 
\f = form feed 
\777 = octal value (must be 1-3 octal digits (0-7)) 
\x41 = hex value (must be two hex digits (x##))
"""
