num_list = []
i = 0
playing = True

while (playing == True):

    num = int(input("Enter an int:"))

    #test if number is -1, to quit the program
    if (num == -1):
        playing = False
    else:
        #add number to list of numbers
        num_list.append(num)
        i += 1

#get the sum of all entered numbers
num_sum = 0
for num in num_list:
    num_sum += num

#calculate the average
num_avg = num_sum / i

print("avg:", num_avg)

    
