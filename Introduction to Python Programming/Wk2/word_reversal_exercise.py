string = 'pasta'
rev = ''

#iterate over a sequence, counting backwards
for j in range(len(string) - 1, -1, -1):

    #concatenate character at index j
    rev += string[j]

print(rev)
