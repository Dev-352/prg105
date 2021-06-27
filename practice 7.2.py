# Using parallel arrays, create a secret code creator.
# Ask the user for text to enter, convert it to the code and write the code to a text file.
# Include punctuation (. , !), space, upper, and lower case letters.

def main():
    # letter that will be converted to code
    code = ['!', '@', '1', '3', '#', '4', '$', '5', '%', '6', '^', '7', '&', '8',
            '*', '9', '(', '0', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|',
            ':', ';', ',', '<', '.', '>', '/', '?', 'q', 'r', 't', 'w', 'i', 'a',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', 'h', 'j', 'f', 'g', 's', 't', 'y']

    # alphabets
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
             'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '!', '$']

    # empty list to put in data
    outline = []

    # print out the context
    print("This program will take whatever sentence you create, and convert it into a secret code.\n It will also"
          " write that code to a text file\n")

    # getting in the message the need to be converted into code
    msg = input("Enter the message you want to be converted into code: ")

    # using for loop to convert letter into code
    for letter in msg:
        letter_index = alpha.index(letter)
        code_v = code[letter_index]
        outline.append(code_v)

        # opening a write file to insert the code
        outfile = open("code.txt", "w")
        for item in outline:
            outfile.write(str(item) + "\n")
        outfile.close()
        # file closed


main()
