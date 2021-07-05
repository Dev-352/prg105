# Read both files into lists. Print the complete customer information on the screen if they are on both lists.
# Do error checking for file names to make sure the files exist (try and except statements.)


def main():
    try:
        file1 = open("accounts.txt", "r")
        file2 = open("over90.txt", "r")

        for line in file1:
            line = line.rstrip("\n")
            split = line.split()
            code = split[0]
            code = code.rstrip(",")

            # print(code)

            for line2 in file2:
                line2 = line2.rstrip("\n")
                split2 = line2.split()
                code2 = split2[0]
                # print("printing line2: " + str(code2))
                if code == code2:
                    print(line)
        file1.close()
        file2.close()
    except IOError:
        print("Invalid file")


main()
