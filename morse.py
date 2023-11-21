# the program will start by displaying a menu 

def english_to_morse(source):

    result = ""

    source = source.upper()

    for letter in source:

        if letter == "A":
            result += ".-"
        
        if letter == "B":
            result += "-..."

        if letter == "C":
            result += "-.-."

        # to do - add other characters

        if letter == "D":
            result += "-.."

        if letter == "E":
            reuslt += "."
        
        if letter == "F":
            result += "..-."

        if letter == "G":
            result += "--."

        if letter == "H":
            result += "...."

        if letter == "I":
            result += ".."

        if letter == "J":
            result += ".---"

        if letter == "K":
            result += "-.-"

        if letter == "L":
            result += ".-.."

        if letter == "M":
            result += "--"

        if letter == "N":
            result += "-."

        if letter == "O":
            result += "---"

        if letter == "P":
            result += ".--."

        if letter == "Q":
            result += "--.-"

        if letter == "R":
            result += ".-."

        if letter == "S":
            result += "..."

        if letter == "T":
            result += "-"

        if letter == "U":
            result += "..-"

        if letter == "V":
            result += "...-"

        if letter == "W":
            result += ".--"

        if letter == "X":
            result += "-..-"

        if letter == "Y":
            result += "-.--"

        if letter == "Z":
            result += "--.."

        if letter == " ":
            result += " "

        result += " "

    return result

print(english_to_morse("ATTACK AT DAWN"))