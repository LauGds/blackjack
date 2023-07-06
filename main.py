############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose\n"
  elif user_score == computer_score:
    return "It's a draw\n"
  elif computer_score == 0 or computer_score == 21:
    return "You lose, opponent has Blackjack\n"
  elif user_score == 0 or user_score == 21:
    return "You Win with a Blackjack\n"
  elif user_score > 21:
    return "You went over, you lose\n"
  elif computer_score > 21:
    return "Opponent went over, You win\n"
  elif user_score > computer_score:
    return "You win\n"
  else:
    return "You lose\n"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
      is_game_over = True
    else:
      continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
      if continue_game == "y":
        user_cards.append(deal_card())
      elif continue_game == "n":
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play Blackjack game? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()
