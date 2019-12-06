#Contains string and list of 49 words and functions
words = """
Awkward
Bagpipes
Banjo
Bungler
Croquet
Crypt
Dwarves
Fervid
Fishhook
Fjord
Gazebo
Gypsy
Haiku
Haphazard
Hyphen
Ivory
Jazzy
Jiffy
Jinx
Jukebox
Kayak
Kiosk
Klutz
Memento
Mystify
Numbskull
Ostracize
Oxygen
Pajama
Phlegm
Pixel
Polka
Quad
Quip
Rhythmic
Rogue
Sphinx
Squawk
Swivel
Toady
Twelfth
Unzip
Waxy
Wildebeest
Yacht
Zealous
Zigzag
Zippy
Zombie
"""
words = words.lower() #removes uppercase characters
list_of_words = words.split() #creates list from string and sets each word into a separate element

def print_playfield(playfield):
  for i in playfield:
    print(i, end = " ")

#creates function that returns the indices of each instance of a specific character in in string
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]