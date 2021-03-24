def vowel_counter(string):
    """Counts the number of vowels in given string."""

    vowel_count = count_instance_of_str(string, 'aeiou')

    return vowel_count

def word_counter(sentence):
    """Counts the number of words in given sentence."""

    sentence = sentence.strip() #removes whitespace from beginning and end of sentence

    num_spaces = count_instance_of_str(sentence, ' ')

    word_count = num_spaces + 1

    return word_count

def count_instance_of_str(string1, string2):
    """Counts characters in string1 that are also in string2."""

    count = 0

    #for each char in string1, check if it's in string2
    for char in string1:
        if char in string2:
            count += 1

    return count
    
     
def main():

    while 1 == 1:

        input_string = input("enter a string: ")

        if input_string == '-1':
            break

        print(vowel_counter(input_string), "vowels in", input_string)
        #print(word_counter(input_string), "words in", input_string)


#to execute main function
if __name__ == '__main__':
    main()
