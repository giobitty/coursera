name = input("What is your name? ")
print("Hello "+ name)
birth_year = int(input("Year of birth "))
age = 2024 - birth_year
if(age > 21):
 print( "You are " + str(age) + "years old")
else:
 print("Not age appropriate")
exit()