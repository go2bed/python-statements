##Use for, split(), and if to create a Statement that
#  will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
lst = st.split(' ')
for word in lst:
    if word[0] == 's':
        print(word)

# Write a programm that prints numbers from 0 to 100. But for
# multiples of three print 'Fizz' instead of number and for
# multiples of 5 print 'Buzz', for multiples of each one print
# 'FizzBuzz'

l = list(range(101))

for num in l:
    if num % 3 == 0 and num % 5 == 0:
        print('Fizz!')
    elif num % 5 == 0:
        print('Buzz!')
    elif num % 3 == 0:
        print('FizzBuzz!')
    else:
        print(num)

# Use List comprehension to create a list of all numbers
# between 1 and 50 that are divisible by 3.
l = [num for num in range(50) if num % 3 == 0]
print(l)

# Use List comprehension to create a list
# of the first letters of evey word in the string below
st = 'Create a list the first letters of each word in this string'
l = [letter[0] for letter in st.split(' ')]
print(l)


