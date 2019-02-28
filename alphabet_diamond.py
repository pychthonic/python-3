def print_alphabet_diamond(letter, outside_char, inside_char):
    
    if letter.islower():
        letter_num = ord(letter) - 96
        alphabet = "abcdefghijklmnopqrstuvwxyz"

    elif letter.isupper():
        letter_num = ord(letter) - 64
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    width = 2 * letter_num - 1 + (letter_num - 1) * 2
    for i in range(letter_num - 1, 0, -1):
        letters = alphabet[letter_num - 1]
        if i < (letter_num - 1):
            for j in range(letter_num - 2, i - 1, -1):
                letters += inside_char
                letters += alphabet[j]
            for j in range(i + 1, letter_num):
                letters += inside_char
                letters += alphabet[j]
        print(letters.center(width, outside_char))
    letters = ''
    for i in range(letter_num - 1, 0, -1):
        letters += alphabet[i]
        letters += inside_char
    letters += alphabet[0]
    for i in range(1, letter_num):
        letters += inside_char
        letters += alphabet[i]
    print(letters)
    for i in range(1, letter_num):
        letters = alphabet[letter_num - 1]
        if i < letter_num - 1:
            for j in range(letter_num - 2, i, -1):
                letters += inside_char
                letters += alphabet[j]
            for j in range(i, letter_num - 1):
                letters += inside_char
                letters += alphabet[j]
            letters += inside_char + alphabet[letter_num - 1]
        print(letters.center(width, outside_char))

if __name__ == '__main__':
    letter = ''
    outside_char = ''
    inside_char = ''
    while not letter.isalpha() or len(letter) > 1:
        letter = input(
            "What letter would you like the alphabet diamond to go up to?"
            "\n Enter a-z for lowercase, A-Z for uppercase: ")
        if not letter.isalpha():
            print(f"{letter} is not a letter.")
        if len(letter) > 1:
            print("Singles only.")
    while len(outside_char) != 1:
        outside_char = input(
            "What character would you like to use to fill the empty space"
            " outside the diamond? (press enter for nothing) ")
        if outside_char == '':
            outside_char = ' '
        elif len(outside_char) > 1:
            print("Singles only.")
    while len(inside_char) != 1:
        inside_char = input(
            "Enter character to fill the empty space inside the diamond?"
            " (press enter for nothing) ")
        if inside_char == '':
            inside_char = ' '
        elif len_inside_char > 1:
            print("Singles only.")
    print_alphabet_diamond(letter, outside_char, inside_char)
