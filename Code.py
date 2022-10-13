def code(p1: str) -> int:
    #actually does the convertion but gives binary in alist
    dictionary = {"a": 00000, "e": 00001, "i": 00010,"o": 00011, "u": 00100, "r": 00101, "s": 00110, "t": 00111, "n": 01000, "l": 01001, "T": 01010, ",": 01100, ".": 01101, "!": 01110, "?": 01111, " ": 01011}  #char to bin
    bin = []  #this is what will be returned//a list of the converted char into binary
    for char in p1:  #goes through every char in the string
        if char in dictionary: #checking to see if the char is actuallly given a val in the dictionary
            result = dictionary[char]  #goes into dict and checks to see what char is equal to
            bin.append(result)  #adds binary number to the list bin for ever char

            #following code concatinates all the binary numbers into int

            final = "" #need this outside to be able to make list into str
            count = 0
            for num in bin:
                final = final + str(num)
                count = count+1 #keeps track of num of characters being converted
            final = int(final)

    print(count,".",final)  #this is the final output// should be a list of all the chars values as binary
