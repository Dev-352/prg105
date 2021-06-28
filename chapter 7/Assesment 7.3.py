# For this assessment we are decoding a file from user


def main():

    code = ['!', '@', '1', '3', '#', '4', '$', '5', '%', '6', '^', '7', '&', '8',
            '*', '9', '(', '0', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|',
            ':', ';', ',', '<', '.', '>', '/', '?', 'q', 'r', 't', 'w', 'i', 'a',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', 'h', 'j', 'f', 'g', 's', 't', 'y']

    # alphabets
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
             'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '!', '$']

    print("This program will decode a coded text file.\n")
    # getting in file name
    file = input("What is the name of the file to decode? ")
    # setting the list
    inline = []
    # using a try statement to check if the file exists or not
    try:
        # opens the file and read the file
        f = open(file, 'r')
        s = f.readlines()
        # converting code to english using a for loop
        for lines in s:
            line = lines.strip('\n')
            letter_index = code.index(line)
            alpha_a = alpha[letter_index]
            inline.append(alpha_a)
        # closing the file
        f.close()
        # writing code into a file
        outfile = open("decode.txt", 'w')
        for item in inline:
            outfile.write(str(item))
        outfile.close()
        # outputting code
        read = open("decode.txt", 'r')
        r = read.readlines()
        for lines in r:
            print(lines)
    except IOError:
        print("File not found")


main()
