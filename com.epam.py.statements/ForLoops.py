l = [1, 2, 3, 4, 5]

for element in l:
    print(element)

for element in l:
    print("something!")

# MODULO
print(10 % 3)
print(18 % 7)
print(4 % 2)

for element in l:
    print("****")
    if element % 2 == 0:
        print("Here is an even")
    else:
        print("Odd number!")

##########Sum
l = [1, 2, 3, 4, 5]
list_sum = 0
for num in l:
    list_sum += num

print('The sum of the list numbers is : ' + list_sum.__str__())

## go through the string by the loop
s = 'This is a string'

for letter in s:
    print(letter)

## go through the tuple by the loop
tup = (1, 2, 3, 4, 5)

for t in tup:
    print(t)

# Tuple unpacking

l = [(2, 4), (6, 8), (10, 12)]

for tup in l:
    for num in tup:
        print(num)  # Go down to the values of tuples

for (t1, t2) in l:
    print(t1)  ## almost the same, but the code is shorter
print("***********")

## FOR Loops for dictionaries
d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)

print("***********")

for k, v in d.items():  ##in python 2 it is d.iteritems()
    print(k)
    print(v)
