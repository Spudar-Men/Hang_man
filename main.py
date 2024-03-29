from string_of_words import list_of_words
from string_of_words import print_playfield
from string_of_words import find
from more_itertools import locate
import random
import replit


rand_word = random.choice(list_of_words) #draws random word from list out 49 possible words
print("Cheat mode on. Word is: " + rand_word)

indexPosList = 0
playfield = []
for letter in rand_word:
  playfield.append("[_]")
print_playfield(playfield)
print()

player_guess = "" #create empty string that will contain imput from player
win = False #Starts at False and is changed when win state is achieved
player_attempts = 3
print("Len of playfield is " + str(len(playfield)))
player_guess = ""
while player_attempts > 0 and win == False:
  print("Player Attempts: " + str(player_attempts))
  while len(player_guess) != 1 or player_guess == "":
    player_guess = input("Please guess one letter from the secret Hangman word: ")
  for letter in rand_word:
    if letter == player_guess:
      indexPosList = list(locate(rand_word, lambda a: a == letter))
      for item in indexPosList:
        playfield[item] = letter
  if player_guess not in rand_word:
    player_attempts -= 1
  replit.clear()
  print_playfield(playfield)
  print()
  player_guess = ""
  if "[_]" not in playfield:
    win = True
else:
    if win == True:
      print("You Won!")
    else:
      print("You Lost!")