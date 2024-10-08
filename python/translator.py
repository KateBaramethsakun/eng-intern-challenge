import sys


braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.O..OO', 'capital': '.....O', 'number': '.O.OOO'
}


reverse_dict = {v: k for k, v in braille_dict.items()}

def translate(input_text):
    if all(c in 'O.' for c in input_text):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)

def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(braille_dict['capital'])
            char = char.lower()
        if char.isdigit() and not number_mode:
            result.append(braille_dict['number'])
            number_mode = True
        elif not char.isdigit():
            number_mode = False
        result.append(braille_dict.get(char, '......'))
    
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    number_mode = False

    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_dict['capital']:
            result.append(reverse_dict[braille[i+6:i+12]].upper())
            i += 12
        elif symbol == braille_dict['number']:
            number_mode = True
            i += 6
        else:
            letter = reverse_dict.get(symbol, '')
            if number_mode and letter.isalpha():
                number_mode = False
            result.append(letter)
            i += 6

    return ''.join(result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
        print(translate(input_string).strip())  
    else:
        print("Please provide an input string to translate.")

