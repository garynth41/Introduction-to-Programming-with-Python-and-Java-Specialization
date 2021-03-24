#exit a loop using continue

for number in range(1, 21):

    #test for odd number
    if (number % 2 != 0):

        #test for multiple of 3
        if (number % 3 == 0):
            continue

        print(number)
            
        
        
