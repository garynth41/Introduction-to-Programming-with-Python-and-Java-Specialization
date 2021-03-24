name = input("What is your first name?")

letter_count = 0

print(name, "is spelled:")
for x in name:
    print(x, end = ' ')
    letter_count += 1

print("")
print(letter_count, "letters in the name", name)
