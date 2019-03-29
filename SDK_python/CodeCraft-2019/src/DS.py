import networkx as nx
import Road as rd
import Cross as cr
import Car as ca
import functools

class Net:
    def __init__(self, car_path, cross_path, road_path):
        self.G = nx.DiGraph()
        self.answers = []
        washer =  lambda x:[int(i) for i in x.replace('(','').replace(')','').split(",")]

        with open(car_path) as f:
            [ca.addCar(ca.CarInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']

        with open(cross_path) as f:
            [cr.addCross(cr.CrossInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']

        with open(road_path) as f:
            [rd.addRoad(rd.RoadInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']

        
        for road in rd.RoadList:
            if  road.isDuplex == 1:
                self.G.add_weighted_edges_from([(road.From, road.to, road.length), (road.to, road.From, road.length)])
            else:
                self.G.add_weighted_edges_from([(road.From, road.to, road.length)])
        
    
    def find_route(self):
        for c in ca.CarList:
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
        
