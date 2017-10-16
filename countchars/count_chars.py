# Create a function that takes the filepath (e.g. "da_vinci_code.txt") as an input, reads the given file, and counts the occurences of 0, 1 and x characters in it.
# The function should return a dictionary in which the searched characters are the keys and the number of their occurences are the values.
# Use the uploaded da_vinci_code.txt file in this folder on GitHub to test your program.
# For example:
#
# countedLetters = countLetters("da_vinci_code.txt");
# print("0 occured " + countedLetters["0"] + " times in the file.");
# print("1 occured " + countedLetters["1"] + " times in the file.");
# print("x occured " + countedLetters["x"] + " times in the file.");
# 
# Should print:
# 0 occured 3393 times in the file.
# 1 occured 3375 times in the file.
# x occured 3232 times in the file.


def reading_file(file_name):
    with open('D:\greenfox\pallida-basic-retake-exam\countchars\da_vinci_code.txt', 'r') as used_file:
        used_file = used_file.read()
        return used_file


def counted_letters(used_file):
    letter_counter = {}
    letters = reading_file('da_vinci_code.txt')
    for letter in letters:
        if letter not in letter_counter:
            if letter == "0":
                letter_counter["0"] = 1
            elif letter == "1":
                letter_counter["1"] = 1
            elif letter == "x":
                letter_counter["x"] = 1
        else:
            if letter == "0":
                letter_counter["0"] += 1
            elif letter == "1":
                letter_counter["1"] += 1
            elif letter == "x":
                letter_counter["x"] += 1
    return letter_counter


countedLetters = counted_letters("da_vinci_code.txt")
print("0 occured " + str(countedLetters["0"]) + " times in the file.")
print("1 occured " + str(countedLetters["1"]) + " times in the file.")
print("x occured " + str(countedLetters["x"]) + " times in the file.")
