import art
import random
from game_data import data
from replit import clear


def entries(list):
  """Randomly chooses an entry from the list provided."""
  entry_list = []
  entry = random.choice(list)
  for element in entry.values():
    entry_list.append(element)
  return entry_list

def compare_followers(first_entry, second_entry):
  """Comparing the followers of the two randomly chosen entries and
   returning the entry with less followers."""
  if first_entry[1] > second_entry[1]:
    return second_entry
  else:
    return first_entry

game_over = False
entry_A = entries(data)
counter = 0
  
while not game_over:
  print(art.logo)
  
  entry_B = entries(data)
  lowest_followers = compare_followers(entry_A, entry_B)
  print(lowest_followers)
  if counter != 0:
    print(f"Your score is {counter}")
  print(f"Compare A: {entry_A[0]}, {entry_A[2]}, from {entry_A[3]}")
  print(art.vs)
  print(f"Against B: {entry_B[0]}, {entry_B[2]}, from {entry_B[3]}")
  answers = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  if answers == 'A':
    if lowest_followers == entry_A:
      print(f"Sorry, wrong answer. Your final score is {counter}")
      game_over = True
    else:
      entry_A = entry_B
  elif answers == 'B':
    if lowest_followers == entry_B:
      print(f"Sorry, wrong answer. Your final score is {counter}")
      game_over = True
    else:
      entry_A = entry_B
  counter += 1
  clear()