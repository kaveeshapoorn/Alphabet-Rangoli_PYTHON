def printRangoli (n):
    for i in range (n):                                                                 # traverse row upper part of the pattern
        print ("--" * (n - 1 - i), end="")                                              # initial spaces  

        if i != 0:                                                                      # left side of the middle column
            for j in range (i):                                         
                print (chr (97 + (n - 1) - j), "-", sep="", end="")                     # alphabets

        print (chr (97 + n - 1 - i), end="")                                            # middle column

        if i != 0:                                                                      # right side of the middle column
            for j in range(i):
                print("-", chr(97 + (n - 1) - i + (j + 1)), sep="", end="")             # alphabets 

        print ("--" * ((n - 1) - i))                                                    # final spaces

    for i in range(n-2, -1, -1):                                                        # lower part of the pattern
        print("--" * (n - 1 - i), end="")                                               # initial spaces

        if i != 0:                                                                      # left side of the middle column
            for j in range (i):
                print (chr (97 + (n - 1) - j), "-", sep="", end="")                     # alphabets

        print (chr (97 + (n - 1) - i), end="")                                          # middle column

        if i != 0:                                                                      # right side of the middle column
            for j in range (i):
                print ("-", chr (97 + (((n - 1) - i)) + j + 1), sep="", end="")         # alphabets       

        print("--" * (n - 1 - i))                                                       # final spaces

if __name__ == "__main__":
    size = int (input ())
    printRangoli (size)
