# String data type

first = "ciao"
last = "bella"

# print(type(first))
# print(isinstance(first, str))

#construction function
# pizza = str("pepperoni")
# print(type(pizza))
# print(isinstance(pizza, str))

# concatenation 
greeting = first + " " + last
print(greeting)

#casting
decade = str(2020)
print(type(decade))
print(decade)

#multiple lines with 3 single quotes '''  theStatements  '''
multiline = '''
Hey, come va?                                          
Era solo per sapere.        
                            Tutto bene?
                            
'''

print(multiline)

#String methods
#.lower() =>lower case  .upper()=> upper case    .title()=> capitalize every fist letter .replace()=> replaces

#build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1")
print("Muffin".ljust(16, ".") + "$2")
print("Cheese cake".ljust(16, ".") + "$1.75")

#built in functions for numbers
#int constructor int(variable)
# import math and use math.variable ex math.pi  ;  print(math.sqrt())  ; math.floor(gpa)