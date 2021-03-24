#define list of numbers
numbers = [5, 3, 8, -1, -2.2, 0]

#define min number variable
min_number = numbers[0]

#find the minimum value
for number in numbers:
    #check if the number is less than the defined min number (above)
    if number < min_number:
        #reset min number
        min_number = number

print(min_number, "is the min number")

    

