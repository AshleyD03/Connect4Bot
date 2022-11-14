from grid import Grid
from robot import Robot
from colorama import Fore

# Ensure that the input is an integer
def intInput(msg):
  value = input(msg)
  while (not value.isdigit()):
      value = input('integers only, try again... ')
  return int(value)

def main ():
  # Get difficulty
  difficulty = intInput("How difficult do you want me to be [1-10]?\nEasy [3] Medium [4] Hard [5] ... ")
  while (difficulty < 1 or difficulty > 10):
    difficulty = intInput("Between 1 and 10 please...")

  # Define grid and piece
  grid = Grid(7, 6)
  robot = Robot(difficulty, 'Y', 'X')
  piece = 'X'
  grid.setPieceMap({
    'X': Fore.BLUE + '▇' + Fore.RESET,
    'Y': Fore.RED + '▇' + Fore.RESET
  })
  grid._print();

  # Start game loop & Check if game is over yet
  while (not grid.getWon() and not grid.getDraw()):
    # Ask for column to place piece in
    result = grid._placePiece(intInput("It's your move... "), piece)
    while (result['error']):
      result = grid._placePiece(intInput('invalid answer, give another... '), piece)

    if (result['won'] or grid.getDraw()):
      break
    
    grid._print();
    move = robot._move(grid)
    result = grid._placePiece(move, robot.getPiece())
    grid._print();
    

  # Print game end results
  grid._print();
  print("Difficulty:",str(difficulty))
  if (grid.getWon()):
    if (grid.getWinningPiece() == 'X'):
      print("You... Beat me?\nHow is it even possible...")
    else:
      print("You Lose !!!")
  else:
    print("Tie")


if __name__ == '__main__':
  main()