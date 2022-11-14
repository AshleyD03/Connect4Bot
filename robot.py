"""
  A minimax algorithm to play against.
"""
class Robot:
  def __init__(self, depth, piece, enemyPiece):
    self.__depth__ = depth
    self.__piece__ = piece
    self.__enemyPiece__ = enemyPiece
    self.__counter__ = 0;

  def _move(self, state, depth=0):
    successors = self._successors(state)
    scores = []
    self.__counter__ = 0

    if (depth == 0):
      depth = self.__depth__

    for s in self._successors(state):
      #print(s._recentResult_)
      score = [s._recentResult_['x'], self._minValue(s, depth)]
      #print(score)
      scores.append(score)

    top = scores[0]
    print("I have evaluated ",self.__counter__,"realities")
    print(scores)
    for s in scores:
      if (s[1] > top[1]):
        top = s 

    if (top[1] == -100 and depth > 1):
      return self._move(state, depth - 1)
    else:
      return top[0]


  def _maxValue(self, state, depth):
    if (depth == 0 or state.getWon()):
      #state._print()
      return self._eval(state)
    v = -1000
    for s in self._successors(state):
      m = self._minValue(s, depth - 1)
      #print("min("+str(v)+","+str(m)+")")
      v = max(v, m)
    return v
    

  def _minValue(self, state, depth):
    if (depth == 0 or state.getWon()):
      #state._print()
      return self._eval(state)
    v = 1000
    for s in self._successors(state):
      m = self._maxValue(s, depth - 1)
      #print("min("+str(v)+","+str(m)+")")
      v = min(v, m)
    return v


  def _successors(self, state):
    successors = []
    piece = self.__piece__ 
    if (state._recentResult_['piece'] == piece):
      piece = self.__enemyPiece__
      #print("swap")

    for x in range (state.getWidth()):
      new = state._clone();
      result = new._placePiece(x + 1, piece)
      if (result['error'] == False):
        successors.append(new);
    return successors

  def _eval(self, state):
    recent = state._recentResult_
    self.__counter__ += 1

    # Check if they have a winning move or need to prevent a winning move
    if (state.getWon()):
      #print('winner')
      if (state.getWinningPiece() == self.__enemyPiece__):
        return -100
      return 100

    # If ended because of an error
    if (recent['error']):
      return 0 

    # If the last piece wasn't his, return the score of it to negative
    if (recent['piece'] != self.__piece__):
      return -recent['sum']

    # Else return the score of the last piece he played
    return recent['sum']

  def getPiece(self):
    return self.__piece__