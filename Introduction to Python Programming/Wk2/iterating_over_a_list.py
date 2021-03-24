#define list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#to store even numbers
even_numbers = []

#to store count of even numbers
even_count = 0

#iterate over list 
for number in numbers:
    #test if number is even
    if (number % 2 == 0):
        #append to even numbers list
        even_numbers.append(number)

        #increment count
        even_count += 1

print(even_numbers)
print("There are", even_count, "numbers in the even list.")
print("There are", len(even_numbers), "numbers in the even list.")
