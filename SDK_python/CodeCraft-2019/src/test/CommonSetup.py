
import hwdata.Road as rd
import hwdata.Cross as cr
import hwdata.Car as ca
def SetUp():
    car_path = "../../config/car.txt"
    cross_path = "../../config/cross.txt"
    road_path = "../../config/road.txt"

    washer =  lambda x:[int(i) for i in x.replace('(','').replace(')','').split(",")]


    with open(car_path) as f:
        [ca.addCar(ca.CarInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']

    with open(cross_path) as f:
        [cr.addCross(cr.CrossInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']

    with open(road_path) as f:
        [rd.addRoad(rd.RoadInst(*(washer(x)))) for x in f.readlines() if x[0] !='#']
