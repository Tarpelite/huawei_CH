import networkx as nx

class Car:
    def __init__(self,Id,From,to,speed,planTime):
        self.id = Id
        self.From = From
        self.to = to
        self.speed = speed
        self.planTime = planTime

class Cross:
    def __init__(self,id,rId1,rId2,rId3,rId4):
        self.id = id
        self.rId1 = rId1
        self.rId2 = rId2
        self.rId3 = rId3
        self.rId4 = rId4
    
class Road:
    def __init__(self,id,length,speed,channel,From,to,isDuplex):
        self.id  = id
        self.length = length
        self.speed = speed
        self.channel = channel
        self.From = From
        self.to = to
        self.isDuplex = isDuplex

class Net:
    def __init__(self, car_path, cross_path, road_path):
        self.roads = []
        self.routes = []
        self.G = nx.DiGraph()
        self.answers = []

        with open(car_path) as f:
            self.cars = [Car(*i) for i in f.readlines()]

        with open(cross_path) as f:
            self.crosses = [Cross(*i) for i in f.readlines()]

        with open(road_path) as f:
            self.roads =  [Road(*i) for i in f.readlines()]
        
        for road in self.roads:
            if  road.isDuplex == 1:
                self.G.add_weighted_edges_from([(road.From, road.to, road.length), (road.to, road.From, road.length)])
            else:
                self.G.add_weighted_edges_from([(road.From, road.to, road.length)])
        
    
    def find_route(self):
        for c in self.cars:
            res = [c.id]
            path = nx.dijkstra_path(self.G, c.From, c.to)
            res.extend(path)
            self.answers.append(res)
    
if __name__ == "__main__":
    car_path = "../config/car.txt"
    cross_path = "../config/cross.txt"
    road_path = "../config/road.txt"
    net = Net(car_path, cross_path, road_path)
    net.find_route()
    print(net.answers)
        
