import math


def add_asterisks(text):
    words = text.split()
    result = []

    for word in words:
        length = len(word)
        half = math.ceil(length / 2)
        new_word = '**' + word[:half] + '**' + word[half:]
        result.append(new_word)

    return ' '.join(result)


text_input = input("Enter the text: ")
modified_text = add_asterisks(text_input)
print("Modified text:", modified_text)
