l = []

for letter in 'word':
    l.append(letter)

print(l)

l = [letter for letter in 'word']

print(l)

list = [x ** 2 for x in range(0, 12)]
print(list)

lst = [number for number in range(11) if number % 2 == 0]
print(lst)

celsius = [0, 10, 20.1, 34.5]

fahrenheit = [(temp * (9 / 5) + 32) for temp in celsius]

print(fahrenheit)

# Final result is x**4 for x in range (11)
list = [x ** 2 for x in [x ** 2 for x in range(11)]]
print(list)
