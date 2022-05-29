class GameEmulator:
  def __init__(self, PList, CList):
      self.PList = PList
      self.CList = CList
  
  def baseNumChoice(self):
    return [max(self.PList[i]) for i in range(4)]
  
  def selectedS(self, row, col, num):
    self.CList[row][col] += 1
    self.PList[row][col] += ((self.CList[row][col]-1)*self.PList[row][col]+(num/4))/self.CList[row][col]
    
  def selectedB(self, row, col, num):
      for i in range(4):
          if i == row:
              continue
          self.CList[i][col] += 1
          self.PList[i][col] += ((self.CList[i][col]-1)*self.PList[i][col]+(num/4))/self.CList[i][col]
  
  def selectedBandS(self, B, S):
    for i in range(4):
        if self.PList[i].count(0) == 9:
            S-=1
    if S == 0:
        selectedB(1,1,1)
    self.PList[row][col] += num*W

  def delete(self, row, col):
    self.PList[row][col] = 0
    
  def compare(self, SList, AList):
    return len([SList.pop( i - (8 - len(SList) ) ) for i in range(4) if SList[ i - (8 - len(SList)) ] == AList[i]]) + 10*len(set.intersection(set(AList), set(SList)))
