import hwdata.Road as rd
import hwdata.Cross as cr
import hwdata.Car as ca
from hwalgorithm.graph import HWDijkstra

class Net:
    def __init__(self, car_path, cross_path, road_path):
        self.answers = []
        washer =  lambda x:[int(i) for i in x.replace('(','').replace(')','').split(",")]

        with open(car_path) as f:
            [ca.addCar(ca.CarInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']

        with open(cross_path) as f:
            [cr.addCross(cr.CrossInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']

        with open(road_path) as f:
            [rd.addRoad(rd.RoadInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']

        

    def find_route(self):
        for c in ca.CarList:
            res = [c.id]
            path = HWDijkstra(c.From, c.to)
            res.extend(path)
            self.answers.append(res)
    
if __name__ == "__main__":
    car_path = "/home/tarpe/酋长的工作区/huawei_softChallenge/huawei_CH/SDK_python/CodeCraft-2019/config/car.txt"
    cross_path = "/home/tarpe/酋长的工作区/huawei_softChallenge/huawei_CH/SDK_python/CodeCraft-2019/config/cross.txt"
    road_path = "/home/tarpe/酋长的工作区/huawei_softChallenge/huawei_CH/SDK_python/CodeCraft-2019/config/road.txt"
    net = Net(car_path, cross_path, road_path)
    net.find_route()
    print(net.answers)
        
