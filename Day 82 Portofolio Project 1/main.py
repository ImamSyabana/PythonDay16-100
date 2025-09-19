# Letter to morse code converter  
letter_to_morse = {
    "A": "o -",
    "B": "- o o o",
    "C": "- o - o",
    "D": "- o o",
    "E": "o",
    "F": "o o - o",
    "G": "- - o",
    "H": "o o o o",
    "I": "o o",
    "J": "o - - -",
    "K": "- o -",
    "L": "o - o o",
    "M": "- -",
    "N": "- o",
    "O": "- - -",
    "P": "o - - o",
    "Q": "- - o -",
    "R": "o - o",
    "S": "o o o",
    "T": "-",
    "U": "o o -",
    "V": "o o o -",
    "W": "o - -",
    "X": "- o o -",
    "Y": "- o - -",
    "Z": "- - o o",
    "1" : "o - - - -",
    "2" : "o o - - -",
    "3" : "o o o - -",
    "4" : "o o o o -",
    "5" : "o o o o o",
    "6" : "- o o o o",
    "7" : "- - o o o",
    "8" : "- - - o o",
    "9" : "- - - - o",
    "0" : "- - - - -",
}

querry_input_str = input("Please input the text: \n")

translated_letters = []
for char in querry_input_str:
    #print(char)
    
    try:
        tmp_morse = (letter_to_morse[char.upper()])
    except KeyError:
        tmp_morse = 'error'
    finally:
        translated_letters.append(tmp_morse)


translated_str = "  ".join(translated_letters)
print(translated_str)