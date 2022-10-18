def Code(fn: str) -> str:
    my_file = open(fn)
    p1 = my_file.read()
    #actually does the convertion but gives binary in alist
    dictionary = {"a": '00000', "e": '00001', "i": '00010',"o": '00011', "u": '00100', "r": '00101', "s": '00110',
                  "t": '00111', "n": '01000', "I": '01001', "T": '01010', ",": '01100', ".": '01101', "!": '01110',
                  "?": '01111', " ": '01011', "b": "1000000", "c": "1000001", "d": "1000010", "f": "1000100", "g": "1001000",
                  "h": "1010000", "j": "1100000", "k": "1100001", "l": "1100010", "m": "1100100", "p": "1101000", "q": "1110000",
                  "v": "1110001", "w": "1110010", "x": "1110100", "y":"1111000", "z": "1111001", "A": "1111010", "B": "1111100",
                  "C": "1111101", "D": "1111110", "E": "1111111", "F": "1000011", "G": "1000111", "H": "1001111", "J": "1011111",
                  "K": "1110111", "L": "1011101", "M": "1001001", "N": "1111011", "O": "1001100", "P": "1011010", "Q": "1011000",
                  "R": "1011001", "S": "1010001", "U": "1010100", "V": "1010110", "W": "1010111", "X": "1010011", "Y": "1100011",
                  "Z": "1100101", "0": "1010101", "1": "1011011", "2": "1001101", "3": "1000101", "4": "1001011", "5": "1001010",
                  "6": "1101111", "7": "1101010", "8": "1101110", "9": "1101001", "-": "1101011", "'": "1101100", "\"": "1110101",
                  "\n": "1110110", ":": "1011100", ";": "1011110"}
  #char to bin
    bin = []  #this is what will be returned//a list of the converted char into binary
    for char in p1:  #goes through every char in the string
        if char in dictionary: #checking to see if the char is actuallly given a val in the dictionary
            result = dictionary[char]  #goes into dict and checks to see what char is equal to
            bin.append(result)  #adds binary number to the list bin for ever char

            #following code concatinates all the binary numbers into int

            final = "" #need this outside to be able to make list into str
            count = 0
            for num in bin:
                final = final + num
                count = count+1 #keeps track of num of letters being converted
    result = str(count) + "."+ final

    out = open('BinOutput.txt', 'w+')
    output = result
    out.write(output)

    return result  #this is the final output// should be a list of all the chars values as binary


