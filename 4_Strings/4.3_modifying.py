# python contains b-in methods u can use on strs, detailed below

## '.upper()' = returns the str in upper case
ex1 = "This method returns the str in upper-case"
print(ex1.upper())

### '.lower()' = returns the str in lower case
ex2 = 'this method returns the "str" in lower case'
print(ex2.lower())

#### to remove whitespace: use the '.strip()' method
ex3 = "this  method removes   any  whitespace  in ur entry "
print(ex3.strip())

##### 'replace()' method: replaces str w/ another str
ex4 = "hello nd whaddup world"
print(ex4.replace("h", "aha"))

###### 'split()' method: splits str into substrings if it finds instances of the separator
ex5 = "deconstructs strings into substrings"
print(ex5.split("strings"))
