CrossList=[]
__CrossIndexing={}

class CrossInst:
    def __init__(self,id,rId1,rId2,rId3,rId4):
        self.id = id
        self.rId1 = rId1
        self.rId2 = rId2
        self.rId3 = rId3
        self.rId4 = rId4
        self.roadTuple =(rId1,rId2,rId3,rId4)







def addCross(crossObj:CrossInst):
    CrossList.append(crossObj)
    __CrossIndexing[crossObj.id] = crossObj

def getCross(crossId:int):
    return  __CrossIndexing.get(crossId)

    

