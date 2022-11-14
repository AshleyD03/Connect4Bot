from grid import Grid

# Ensure that the input is an integer
def intInput(msg):
  value = input(msg)
  while (not value.isdigit()):
      value = input('please input an integer: ')
  return int(value)

def main ():
  # Define grid and piece
  grid = Grid(7, 6)
  piece = ''

  # Start game loop & Check if game is over yet
  while (not grid.getWon() and not grid.getDraw()):

    # Change pieces and print grid
    piece = 'Y' if (piece == 'X') else 'X' 
    grid._print();

    # Ask for column to place piece in
    result = grid._placePiece(intInput(piece + "'s turn... "), piece)
    while (result['error']):
      print('invalid input, please try again: ')
      result = grid._placePiece(intInput(piece + "'s turn... "), piece)

  # Print game end results
  grid._print();
  if (grid.getWon()):
    print("Player",grid.getWinningPiece(),"has Won !!!")
  else:
    print("Tie")

if __name__ == '__main__':
  main()