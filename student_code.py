import requests
from crypt import load_text_from_web
from collections import Counter

# Caractères et bi-caractères fixes (de l'énoncé)
bicharacters = ['e ', 's ', 't ', 'es', ' d', '\r\n', 'en', 'qu', ' l', 're', ' p', 'de', 'le', 'nt', 'on', ' c', ', ', ' e',
                'ou', ' q', ' s', 'n ', 'ue', 'an', 'te', ' a', 'ai', 'se', 'it', 'me', 'is', 'oi', 'r ', 'er', ' m', 'ce',
                'ne', 'et', 'in', 'ns', ' n', 'ur', 'i ', 'a ', 'eu', 'co', 'tr', 'la', 'ar', 'ie', 'ui', 'us', 'ut', 'il',
                ' t', 'pa', 'au', 'el', 'ti', 'st', 'un', 'em', 'ra', 'e,', 'so', 'or', 'l ', ' f', 'll', 'nd', ' j', 'si',
                'ir', 'e\r', 'ss', 'u ', 'po', 'ro', 'ri', 'pr', 's,', 'ma', ' v', ' i', 'di', ' r', 'vo', 'pe', 'to', 'ch',
                '. ', 've', 'nc', 'om', ' o', 'je', 'no', 'rt', 'à ', 'lu', "'e", 'mo', 'ta', 'as', 'at', 'io', 's\r', 'sa',
                "u'", 'av', 'os', ' à', ' u', "l'", "'a", 'rs', 'pl', 'é ', '; ', 'ho', 'té', 'ét', 'fa', 'da', 'li', 'su',
                't\r', 'ée', 'ré', 'dé', 'ec', 'nn', 'mm', "'i", 'ca', 'uv', '\n\r', 'id', ' b', 'ni', 'bl']

characters = ['b', 'j', '\r', 'J', '”', ')', 'Â', 'É', 'ê', '5', 't', '9', 'Y', '%', 'N', 'B', 'V', '\ufeff', 'Ê', '?', '’',
              'i', ':', 's', 'C', 'â', 'ï', 'W', 'y', 'p', 'D', '—', '«', 'º', 'A', '3', 'n', '0', 'q', '4', 'e', 'T',
              'È', '$', 'U', 'v', '»', 'l', 'P', 'X', 'Z', 'À', 'ç', 'u', '…', 'î', 'L', 'k', 'E', 'R', '2', '_', '8', 'é',
              'O', 'Î', '‘', 'a', 'F', 'H', 'c', '[', '(', "'", 'è', 'I', '/', '!', ' ', '°', 'S', '•', '#', 'x', 'à', 'g',
              '*', 'Q', 'w', '1', 'û', '7', 'G', 'm', '™', 'K', 'z', '\n', 'o', 'ù', ',', 'r', ']', '.', 'M', 'Ç', '“', 'h',
              '-', 'f', 'ë', '6', ';', 'd', 'ô']

def split_cryptogram(C):

    # Diviser le nombre binaire en octets
    C_split = [C[i:i+8] for i in range(0, len(C), 8)]
    return C_split

bi_character_count = Counter()
character_count = Counter()

url = "https://www.gutenberg.org/ebooks/13846.txt.utf-8"
corpus1 = load_text_from_web(url)
# Tronquer la partie en anglais
corpus1 = corpus1[822:len(corpus1)-18324]
url = "https://www.gutenberg.org/ebooks/4650.txt.utf-8"
corpus2 = load_text_from_web(url)
# Tronquer la partie en anglais
corpus2 = corpus2[822:len(corpus2)-18324]
url = "https://www.gutenberg.org/cache/epub/63267/pg63267.txt"
corpus3 = load_text_from_web(url)
# Tronquer la partie en anglais
corpus3 = corpus3[822:len(corpus3)-18324]

corpus = corpus1 + corpus2 + corpus3

symboles = characters + bicharacters
corpus_length = len(corpus)
corpus_reduit = corpus

# Compter les apparences des caractères et des bicaractères dans le corpus
for bichar in bicharacters:
  bi_character_count[bichar] = corpus.count(bichar)

  # Enlever les bicaractères avant de compter les caractères pour éviter les "overlaps"
  corpus_reduit = corpus_reduit.replace(bichar, '')

for char in characters:
  character_count[char] = corpus_reduit.count(char)

symbol_count = bi_character_count + character_count
# Compiler la fréquence des symboles en pourcentages
symbol_frequency = {symbol: (count / corpus_length) * 100 for symbol, count in symbol_count.items()}

# Cette fonction associe chaque symbole à une séquence de bits en comparant les fréquences
def map_symbols_to_bytes(symbol_freqs, byte_freqs):

  sorted_symbols = sorted(symbol_freqs.items(), key=lambda x: x[1], reverse=True)
  sorted_bytes = sorted(byte_freqs.items(), key=lambda x: x[1], reverse=True)
  # S'il y a moins de 256 différents bytes, peu probables qu'ils représentent des symboles rares
  # en fin de liste
  sorted_symbols = dict(sorted_symbols[:len(sorted_bytes)-1])
  print(sorted_bytes)

  mapping = {}
  # Pour éviter qu'un même octet soit associé à plus d'un symbole, on tient compte des octets utilisés.
  used_bytes = set()

  for symbol, sym_freq in sorted_symbols.items():

    closest_byte = None
    min_diff = float('inf')

    for byte, byte_freq in byte_freqs.items():
      if byte in used_bytes:
        continue  # Ne pas prendre cet octet s'il est déjà utilisé pour un autre symbole

      diff = abs(sym_freq - byte_freq)
      if diff < min_diff:
        closest_byte = byte
        min_diff = diff
      elif diff == min_diff:
         #Prendre le premier octet rencontré si plusieurs octets ont la même fréquence
        closest_byte = closest_byte or byte

     #"Mapper" le symbole et l'octet et ajouter l'octet à la liste d'octets utilisés
    if closest_byte is not None:
      mapping[symbol] = closest_byte
      used_bytes.add(closest_byte)

  return mapping

def decrypt(C):

  C_split = split_cryptogram(C)

  crypto_count = Counter(C_split)

  crypto_frequency = {byte: (count / len(C_split)) * 100 for byte, count in crypto_count.items()}

  dictionary = map_symbols_to_bytes(symbol_frequency, crypto_frequency)

  M=""

  for byte in C_split:
    if byte in dictionary.values():
      M += list(dictionary.keys())[list(dictionary.values()).index(byte)]
    else:
      M += "?"

  return M

