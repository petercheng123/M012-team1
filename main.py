def encode(p1:str)->int:
    #actually does the convertion but gives binary in alist
    dictionary = {"A": 100000, "B": 100001, "C": 100010} #char to bin
    bin = [] #this is what will be returned//a list of the converted char into binary
    for char in p1: #goes through ever char in the string
        if char in dictionary: #checking to see if the char is actuallly given a val in the dict
            result = dictionary[char] #goes into dict and checks to see what char is equal to
            bin.append(result) #adds binary number to the list bin for ever char

            #entire code concatinates all the binary numbers in bin

            final = "" #need this outside to be able to make list into str
            for num in bin:
                final = final + str(num)
    return final #this is the final output// should be a list of all the chars values as binary