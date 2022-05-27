class GameEmulator:
  def __init__(self, PList, CList):
      self.PList = PList
      self.CList = CList
  
  def baseNumChoice(self):
    return [max(PList[i]) for i in range(4)]
  
  def selectedS(self, row, col, num):
    CList[row][col] += 1
    PList[row][col] += ((CList[row][col]-1)*PList[row][col]+(num/4))/CList[row][col]
    
  def selectedB(self, row, col, num):
      for i in range(4):
          if i == row:
              continue
          CList[i][col] += 1
          PList[i][col] += ((CList[i][col]-1)*PList[i][col]+(num/4))/CList[i][col]
  
  def selectedBandS(self, row, col, W):
    PList[row][col] += num*W

  def delete(self, row, col):
    PList[row][col] = 0
