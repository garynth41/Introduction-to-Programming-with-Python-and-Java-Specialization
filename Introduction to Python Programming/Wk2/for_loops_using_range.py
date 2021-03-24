#Iterate over sequence of 10 numbers, 0 - 9
for x in range(10):
    print(x)

print("")

#Iterate over sequence of 10 numbers, 0 - 9
for x in range(0, 10):
    print(x)

print("")

#Iterate over sequence of 6 numbers, 1 - 6
for x in range(1, 7):
    print(x)

print("")

#Iterate over sequence of 5 numbers, 0 - 28, skipping every 6 numbers
for x in range(0, 30, 7):
    print(x)

print("")

#Iterate over sequence of 6 numbers, counting backwards from 5 - 0
for x in range(5, -1, -1):
    print(x)

print("")

#Find the numbers between 1 and 1200 that are odd
odd_numbers = []

for number in range(1, 1201):
    #if odd, append to odd numbers list
    if (number % 2 != 0):
        odd_numbers.append(number)

print(odd_numbers)
 

