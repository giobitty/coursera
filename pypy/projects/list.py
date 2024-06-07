users =['Sara', 'Giovanni', 'Augusto']
#checks if that value is in the list
print("Sara" in users)

users.insert(0, 'Bobby')
print(users)
#add in a certain spot
users[2:2] = ['Eddie','Julio']

#replace

users[1:3] = ['Robert', 'JSP']
print(users)

users.remove('Bobby')
print(users)

del users[0]
print(users)

nums = [4,6,2,0,9,44]
nums.reverse()
print(nums)
print("")
# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))

numscopy = nums.copy()
