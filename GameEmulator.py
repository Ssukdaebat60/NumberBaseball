class GameEmulator:
  def __init__(self, PList, CList):
      self.PList = PList
      self.CList = CList
  
  def baseNumChoice(self):
    return [max(PList[i]) for i in range(4)]
  
  def selectedBorS(self, low, col, num):
    CList[low][col] += 1
    PList[low][col] += ((CList[low][col]-1)*PList[low][col]+(num/4))/CList[low][col]
  
  def selectedBandS(self, low, col, W):
    PList[low][col] += num*W

  def delete(self, low, col):
    PList[low][col] = 0
