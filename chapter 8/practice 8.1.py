def main():
    # input the phrase
    phrase = input("Enter the phrase: ")

    # split the phrase into substrings
    phrase_split = phrase.split()

    acronym = ""

    # iterate through every substring
    for i in phrase_split:
        acronym = acronym + i[0]
    acronym = acronym.upper()

    print("The acronym for your phrase is ", acronym + ".")


main()
