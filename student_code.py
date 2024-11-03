def decrypt(C):

  dictionary = {'b': '10111011', 'j': '10010010', '\r': '10010101', 'J': '11111111', '”': '00101010', ')': '11000110', 'Â': '11010011', 'É': '01010101', 'ê': '01100010', '5': '10100010', 't': '11001010', '9': '01011100', 'Y': '11101011', '%': '01001110', 'N': '01100100', 'B': '10110010', 'V': '00110100', '\ufeff': '11000010', 'Ê': '10101000', '?': '11011101', '’': '11101001', 'i': '01011101', ':': '00011011', 's': '01101100', 'C': '11010010', 'â': '11110110', 'ï': '01100110', 'W': '00010000', 'y': '10000001', 'p': '11110000', 'D': '10101011', '—': '01011001', '«': '01100111', 'º': '11011111', 'A': '11001101', '3': '10111100', 'n': '11001100', '0': '01001111', 'q': '10101001', '4': '00000100', 'e': '11010101', 'T': '01011010', 'È': '10011000', '$': '00011110', 'U': '01110101', 'v': '00111111', '»': '00101011', 'l': '11001011', 'P': '01010000', 'X': '10101101', 'Z': '10110000', 'À': '10011010', 'ç': '11111001', 'u': '11011011', '…': '01000011', 'î': '00110011', 'L': '10001100', 'k': '00010001', 'E': '10100011', 'R': '10000110', '2': '10011110', '_': '10010011', '8': '00001011', 'é': '00010010', 'O': '01101000', 'Î': '10100111', '‘': '11000011', 'a': '00001101', 'F': '10101100', 'H': '11011000', 'c': '11100110', '[': '00110010', '(': '10111000', "'": '00011010', 'è': '01001000', 'I': '10110111', '/': '01110011', '!': '10010001', ' ': '11001111', '°': '00000011', 'S': '10011100', '•': '11111000', '#': '01101110', 'x': '11111110', 'à': '00111010', 'g': '11000111', '*': '11000001', 'Q': '10001110', 'w': '10100101', '1': '11110010', 'û': '00110110', '7': '10101111', 'G': '00101110', 'm': '10000111', '™': '11000100', 'K': '10111001', 'z': '00101111', '\n': '00001100', 'o': '01111110', 'ù': '11111101', ',': '01110100', 'r': '00000110', ']': '10000101', '.': '01111100', 'M': '10001010', 'Ç': '11010110', '“': '11101101', 'h': '11100010', '-': '01000001', 'f': '11001001', 'ë': '11111010', '6': '00100001', ';': '00001111', 'd': '11010001', 'ô': '10110001', 'e ': '00010100', 's ': '00110001', 't ': '01110000', 'es': '01000000', ' d': '11011100', '\r\n': '00100110', 'en': '01101101', 'qu': '11100000', ' l': '00001010', 're': '11001110', ' p': '01001001', 'de': '00100111', 'le': '00001110', 'nt': '01110110', 'on': '00101100', ' c': '00110000', ', ': '00001000', ' e': '10110110', 'ou': '00101101', ' q': '01010100', ' s': '01010110', 'n ': '01010010', 'ue': '01001100', 'an': '10010000', 'te': '01011011', ' a': '11110011', 'ai': '00011000', 'se': '10010100', 'it': '00111101', 'me': '10110100', 'is': '10100110', 'oi': '10111110', 'r ': '01000110', 'er': '00100000', ' m': '10101010', 'ce': '00011100', 'ne': '10011011', 'et': '11111011', 'in': '01101111', 'ns': '11011010', ' n': '01110010', 'ur': '01100001', 'i ': '01100101', 'a ': '00110101', 'eu': '01101010', 'co': '10111111', 'tr': '00111100', 'la': '11110111', 'ar': '10011001', 'ie': '10001101', 'ui': '00101001', 'us': '00000101', 'ut': '11101100', 'il': '01000101', ' t': '01111111', 'pa': '11110001', 'au': '01110111', 'el': '00110111', 'ti': '11100011', 'st': '01010111', 'un': '00101000', 'em': '11001000', 'ra': '01111010', 'e,': '01101001', 'so': '01111001', 'or': '00111000', 'l ': '01001010', ' f': '01111101', 'll': '10000010', 'nd': '11000000', ' j': '00100011', 'si': '11010100', 'ir': '10001011', 'e\r': '10000100', 'ss': '11100001', 'u ': '00000000', 'po': '10100100', 'ro': '11111100', 'ri': '01100011', 'pr': '00111011', 's,': '01110001', 'ma': '00011111', ' v': '11010000', ' i': '11101111', 'di': '10100000', ' r': '10101110', 'vo': '11010111', 'pe': '00000010', 'to': '01101011', 'ch': '00100101', '. ': '01010011', 've': '10111101', 'nc': '01011111', 'om': '01001101', ' o': '00000111', 'je': '11011110', 'no': '10001111', 'rt': '00010011', 'à ': '01011000', 'lu': '10010111', "'e": '10001000', 'mo': '00010110', 'ta': '00100010', 'as': '00010101', 'at': '01011110', 'io': '11110101', 's\r': '00001001', 'sa': '00111001', "u'": '00111110', 'av': '10010110', 'os': '01001011', ' à': '11101110', ' u': '10111010', "l'": '10011111', "'a": '10000000', 'rs': '01000010', 'pl': '01100000', 'é ': '00010111', '; ': '10001001', 'ho': '10011101', 'té': '01111011', 'ét': '00011101', 'fa': '11110100', 'da': '11101000', 'li': '01000111', 'su': '11000101', 't\r': '01000100', 'ée': '10000011', 'ré': '11100111', 'dé': '01111000', 'ec': '11100101', 'nn': '11101010', 'mm': '01010001', "'i": '00100100', 'ca': '11100100', 'uv': '00011001', '\n\r': '10100001', 'id': '11011001', ' b': '10110011', 'ni': '00000001', 'bl': '10110101'}

  C_split = split_cryptogram(C)

  M=""

  for byte in C_split:
    if byte in dictionary.values():
      M += list(dictionary.keys())[list(dictionary.values()).index(byte)]
    else:
      M += "?"
  print(M)

def split_cryptogram(C):

  # Diviser le nombre binaire en octets
  C_split = [C[i:i+8] for i in range(0, len(C), 8)]
  return C_split
