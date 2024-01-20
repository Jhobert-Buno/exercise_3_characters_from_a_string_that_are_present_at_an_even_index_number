# Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

#pseudocode
#ask user input
word = input("Type the word here: ")

#display the word inputted
print("The original word is: ", word)
#range of the word
length = len(word)

#printing the result
('Printing only even index chars')

for i in range(0, length -1, 2):
    print("[",i,"]", word[i])