# Project 2 - Hot Dog Cookout Calculator

people = int(input("How many people are attending? "))
numdogs = int(input("How many hot dogs will be given for each person? "))

dogspack = 10 # the number of hot dogs per package
bunspack = 8  # the number of hot dog buns per package

# "total" is the number of hot dogs needed and the number of hot dog buns needed
total = people * numdogs


# calculate the minimum number of packages of hot dogs needed and 
# the number of hot dogs leftovers
dogspackneeded = total / dogspack
dogsleft= total % dogspack
if dogsleft != 0:
    dogsMinipackneeded = int(dogspackneeded + 1)
    dogsleftover = dogsMinipackneeded * dogspack - total
else:
    dogsMinipackneeded = int(dogspackneeded)
    dogsleftover = 0
    
# calculate the minimum number of packages of hot dog buns needed and 
# the number of hot dog buns leftovers
bunspackneeded = total / bunspack
bunsleft = total % bunspack
if bunsleft != 0:
    bunsMinipackneeded = int(bunspackneeded + 1)
    bunsleftover = bunsMinipackneeded * bunspack - total
else:
    bunsMinipackneeded = int(bunspackneeded)
    bunsleftover = 0

print("The minimum number of packages of hot dogs required: ", dogsMinipackneeded)
print("The minimum number of packages of hot dog buns required: ", bunsMinipackneeded)
print("Hot dogs leftovers: ", dogsleftover)
print("Hot dogs buns leftovers: ", bunsleftover)