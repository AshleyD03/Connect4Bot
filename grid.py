import copy
from colorama import Fore

"""
  A grid to play connect-4 on.
"""
class Grid:
  def __init__(self, width, height):
    self.__rows__ = [ [' ']*width for i in range (height) ]
    self.__won__ = False 
    self.__draw__ = False
    self.__winningPiece__ = ''
    self.__width__ = width; 
    self.__height__ = height;
    self.__checkFull();
    self._recentResult_ = {'error': True, 'msg': 'empty'};
    self.__pieceMap__ = {} 

  # Set the grid to be equal to a set of rows
  def _populate(self, rows):
    self.__rows__ = rows

  def _clone(self):
    new = Grid(self.__width__, self.__height__)
    new._populate(copy.deepcopy(self.__rows__))
    new._recentResult_ = self._recentResult_
    return new

  # Place a piece on the grid, return the status of self._checkGrid at positon
  def _placePiece(self, x, piece):
    x -= 1 

    # Stop if in draw
    if (self.__draw__):
      return {'error': True, 'msg': 'board full'}

    # Stop if in out of bound
    if (x > self.__width__ - 1 or x < 0):
      return {'error': True, 'msg': 'out of bound'}

    y = 0 
    while (self.__rows__[y][x] != ' '):
      y += 1 
      if (y > self.__height__ - 1):
          return {'error': True}

    self.__rows__[y][x] = piece 
    result = self._checkGrid(x, y, piece)

    if (result['won']):
      self.__won__ = True 
      self.__winningPiece__ = piece

    self.__checkFull()
    self._recentResult_ = result;

    return result

  # Print out the grid for users to visualise
  def _print(self):
    # Print the grid
    for line in self.__rows__[::-1]:
      string = ''
      for char in line:
        if char in self.__pieceMap__:
          string += self.__pieceMap__[char] + ' '
        else:
          string += char + ' '
      print(string)
    # Print the number line
    for i in range (7):
      print (str(i+1), end=' ')
    print()

  # Check if the game has been won at the played piece. 
  # Return status of play.
  def _checkGrid(self, x, y, piece):
    horizontal = self.__checkLine(x, y, piece, 1, 0)
    vertical = self.__checkLine(x, y, piece, 0, 1)
    diagonal1 = self.__checkLine(x, y, piece, 1, -1)
    diagonal2 = self.__checkLine(x, y, piece, 1, 1)
    max_ = max(horizontal, vertical, diagonal1, diagonal2)

    return {
      'sum': horizontal + vertical + diagonal1 + diagonal2 - 4,
      'max': max_,
      'won': True if max_ > 3 else False,
      'error': False, 
      'msg': 'placed piece successfully',
      'x': x+1,
      'piece': piece
    }

  # Check if the line v(y-x1) = h(x-y1) contains 4 of the same piece, including the point (x1, y1).
  def __checkLine(self, x1, y1, piece, h, v):
    height = self.__height__ - 1
    width = self.__width__ - 1

    def checkSide (direction):
      n = 0
      for i in range (1,4):
        x = x1 + (h * i * direction)
        y = y1 + (v * i * direction)
        # Out of bounds or wrong piece then stop counting
        """
        print({
          'len': len(self.__rows__),
          'height': height,
          'width': width,
          'y': y,
          'x': x
        })
        """

        if (x < 0 or x > width 
        or y < 0 or y >= height ):
          break

        if (self.__rows__[y][x] != piece):
          break
        n += 1
      return n
    
    return 1 + checkSide(1) + checkSide(-1)

  # Chekc if the board is full, if so go into draw mode
  def __checkFull(self):
    for y in range(self.__height__):
      for x in range(self.__width__):
        if (self.__rows__[y][x] == ' '):
          return False
    
    self.__draw__ = True
    return True

  # Get if the game has been won
  def getWon(self):
    return self.__won__

  # Get the winning piece
  def getWinningPiece(self):
    return self.__winningPiece__

  # Get the width of the grid 
  def getWidth(self):
    return self.__width__

  # Get the status of if the game is a draw
  def getDraw(self):
    return self.__draw__

  # Set the piece map of the grid
  def setPieceMap(self, pieceMap):
    self.__pieceMap__ = pieceMap;