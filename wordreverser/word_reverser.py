# Create a function that takes a sentence as an input, reverses the letters in every word (but not reverses the words order in the sentence), and returns the sentence with the reversed words.
# You shouldn't care about upper or lower case letters.
# Example:
#
# reversedWords = reverse_words("lleW ,enod taht saw ton taht drah");
# print(reversedWords);
#
# Should print:
# Well done, that was not that hard

def reverse_words(sentence):
    sentence = list(sentence.split(" "))
    result_sentence = []
    for string in sentence:
        reversed_string = string[::-1]
        result_sentence.append(reversed_string)
    return result_sentence
    


reversedWords = reverse_words("lleW ,enod taht saw ton taht drah")
print(reversedWords)