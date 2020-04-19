import random
def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_sum = 0
  dice_size = int(input('How many sides are the dice? '))
  player = int(input('how many players are there? '))
  for x in range(0,player):
    print(f'player { x+1 }\'s press s to roll')
    y = str(input())
    if y == 's': 
      for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1:
          print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
          print(f'You rolled a {roll}! Critical Success!')
        else:
          print(f'You rolled a {roll}')
      print(f'You have rolled a total of {dice_sum}')
    else:
      print('skiped your turn')
  
if __name__== "__main__":
  main()
