def decode(p1: str) -> str:
    char = []
    long_dictionary = {"1000000": "b", "1000001": "c", "1000010": "d", "1000100": "f", "1001000": "g", "1010000": "h", "1100001": "k", "1100010": "l", "1100100": "m", "1101000": "p", "1110000": "q", "1110001": "v", "1110010": "w", "1110100": "x", "1111000": "y", "1111001": "z", "1111010": "A", "1111100": "B", "1111101": "C", "1111110": "D", "1111111": "E", "1000011": "F", "1000111": "G", "1001111": "H", "1011111": "J", "1110111": "K", "1011101": "L", "1001001": "M", "1111011": "N", "1001100": "O", "1011010": "P", "1011000": "Q", "1011001": "R", "1010001": "S", "1010100": "U", "1010110": "V", "1010111": "W", "1010011": "X", "1100011": "Y", "1100101": "Z", "1010101": "0", "1011011": "1", "1001101": "2", "1000101": "3", "1001011": "4", "1001010": "5", "1101111": "6", "1101010": "7", "1101110": "8", "1101001": "9", "1101011": "-", "1101100": "'", "1110101": "\"", "1110110": "\n", "1011100": ":", "1011110": ";"}
    short_dictionary = {"00000": "a", "00001": "e", "00010": "i", "00011": "o", "00100": "u", "00101": "r", "00110": "s", "00111": "t", "01000": "n", "01001": "I", "01010": "T", "01011": " ", "01100": ",", "01101": ".", "01110": "!", "01111": "?"}
    first_letter = p1[0]
    while p1 != "": # when p1 is not empty
        if first_letter == "1": # if the first number is 1
            first_char = p1[:7] # look at the first 7 digit
            result = long_dictionary[first_char] # search for numbers in the long dictionary and turn them into characters
            char.append(result) # output result in list called char
            p1 = p1.replace(first_char, "") # replace the 7 digits with empty string, basically removing them out of p1
        elif first_letter == "0": # if the first digit is not 1 but 0
            first_char = p1[:5] # look at the first 5 digit
            result = short_dictionary[first_char] # search for the numbers in short dictionary and turned them into characters
            char.append(result) # output result in the list called char
            p1 = p1.replace(first_char, "") # replace the 5 digits with an empty string, basically removing them out of p1


    return "".join(char) # output as text instead of list

v1 = decode("00100010010101101110")
print(v1)

