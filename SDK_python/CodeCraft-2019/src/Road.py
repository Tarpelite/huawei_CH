RoadList=[]
__RoadIndexing={}

class RoadInst:
    def __init__(self,id,length,speed,channel,From,to,isDuplex):
        self.id  = id
        self.length = length
        self.speed = speed
        self.channel = channel
        self.From = From
        self.to = to
        self.isDuplex = isDuplex


def addRoad(road:RoadInst):
    RoadList.append(road)
    __RoadIndexing[road.id] = road

def getRoad(roadId:int):
    # find Road in O(1)
    return __RoadIndexing.get(roadId)
