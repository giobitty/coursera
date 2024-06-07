print("######### nomi ########")

names = ['John', 'Bob', 'Sam', 'Mosh']
#you can even call a [-2] index, this means that is the one before the last
#names[0:3] will print the first 3 positions ( 0 - 1- 2)
print(names[0:3])
#names.clear() doesnt expect any value and will clear the list
# len() => built in functions that returns the number of elements in the list

print("######### ciclo for ########")

numbers = [1,2,3,4,7,9,5]
#to print the numbers of the list this is the quickest code, we could use a while as well
for item in numbers:
    print(item)
# with a while cycle
print("######### ciclo while ########")

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i+1

print("######### range() ########")

#range() functions that returns an object, 

for numero in range(5, 10, 2):
    print(numero)