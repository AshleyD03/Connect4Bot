"""
  Print out a readable verson of the grid.
"""
def printGrid (grid):
  for line in grid[::-1]:
    print(' '.join(line))
  print('1 2 3 4 5 6 7')
  return

"""
  Check if the grid has currently got a win condition due a specified piece.
"""
def checkGrid(grid, x, y, piece):
  horizontal = checkLine(grid, x, y, piece, 1, 0)
  vertical = checkLine(grid, x, y, piece, 0, 1)
  diagonal1 = checkLine(grid, x, y, piece, 1, -1)
  diagonal2 = checkLine(grid, x, y, piece, 1, 1)
  return max(horizontal, vertical, diagonal1, diagonal2)


def checkLine(grid, x, y, piece, h, v):
  height = len(grid)
  width = len(grid[0])
  count = 1;

  def checkSide (multiply):
    n = 0
    for i in range (1,4):
      x1 = x + (h * i * multiply)
      y1 = y + (v * i * multiply) 
      # Out of bounds or touching piece
      if (x1 < 0 or x1 >= width 
      or y1 < 0 or y1 >= height 
      or grid[y1][x1] != piece):
        break
      n += 1
    return n
  
  count += checkSide(1) + checkSide(-1)
  print(count)
  return count

"""
  Place a piece on the grid provided in column X.
  Return either 'error', 'placed' or 'win' as return conditions.
  This calls checkGrid to see if the piece has finished the game.
"""
def placePiece (grid, piece, x):
  x = int(x) - 1;

  if (x > 6):
    return 'error'

  y = 0;
  while (grid[y][x] != ' '):
    y += 1;
    if (y > 5):
      return 'error'

  grid[y][x] = piece
  return checkGrid(grid, x, y, piece)



"""
  Main game loop
  Take turns asking for columns to place pieces in.
  If they updated grid returns a win status, end the game.
"""
def main ():
  grid = [ [' ']*7 for i in range (6) ]
  winner = False
  player = 'X'

  printGrid(grid)
  while (winner == False):

    # Ask for column to place piece in
    result = placePiece(grid, player, input(player + "'s turn... "))
    while (result == 'error'):
      print('invalid input, please try again: ')
      result = placePiece(grid, player, input(player + "'s turn... "))
       
    # Print the game status
    printGrid(grid)

    # Check if they have won, else rotate to next player 
    if (str(result) == "4") :
      winner = True
    elif (player == 'X') :
      player = 'Y'
    else :
      player = 'X'

  print("Player",player,"has Won !!!")
  
if __name__ == '__main__':
  main()


   | 0 | 0 |   |   |   |
---+---+---+---+---+---+---
   | 0 | 0 | F |   |   | 
