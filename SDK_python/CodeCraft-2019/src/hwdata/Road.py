import  hwdata.Cross as cr

RoadList=[]
__RoadIndexing={}

class RoadInst:
    UNACCESS =0
    STRAIGHT =1
    LEFT=2
    RIGHT=3
    RELATION_TABLE={
        1:RIGHT,
        2:STRAIGHT,
        3:LEFT,
        10:RIGHT,
        12:LEFT,
        13:STRAIGHT,
        20:STRAIGHT,
        21:RIGHT,
        23:LEFT,
        30:LEFT,
        31:STRAIGHT,
        32:RIGHT
    } # to avoid a lot  if else


    def __init__(self,id,length,speed,channel,From,to,isDuplex):
        self.id  = id
        self.length = length
        self.speed = speed
        self.channel = channel
        self.From = From
        self.to = to
        self.isDuplex = isDuplex

    def __mod__ (self,other):
        selfTo = cr.getCross(self.to) #type:cr.CrossInst
        otherFrom = cr.getCross(other.From)

        if selfTo is not otherFrom:
            return self.UNACCESS
        else:
            g = lambda x:selfTo.roadTuple.index(x)
            indicator=10*g(self.id)+g(other.id)
            return self.RELATION_TABLE[indicator]


def addRoad(road:RoadInst):
    RoadList.append(road)
    __RoadIndexing[road.id] = road

def getRoad(roadId:int):
    # find Road in O(1)
    return __RoadIndexing.get(roadId)
