Weight = 0.05
SecretNum = 1478

class caseNum:
    def __init__(self, ID):
        self.ID = ID;
        self.calledNum = 0;
        self.percentage = 0.2;
    
    def getID():
        return self.ID
    
    def getCalledNum():
        return self.calledNum
    
    def getPercentage():
        return self.percentage
    
    def delete():
        self.ID=0
    
    def incPerc(num):
        self.calledNum += 1
        self.percentage = ((calledNum-1)*self.percentage+(num/4))/calledNum
    
    def incPercWeight(num):
        self.percentage += num*Weight

if __name__=="__main__":
    ballList = [[caseNum(j) for j in range(10)]for i in range(4)]
