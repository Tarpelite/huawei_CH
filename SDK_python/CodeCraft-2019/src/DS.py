class Car:
    def __init__(self):
        self.id = 0
        self.From = 0
        self.to = 0
        self.speed = 0
        self.planTime = 0
    
    def set_info(self, data:list):
        self.id = int(data[0])
        self.From = int(data[1])
        self.to = int(data[2])
        self.speed = int(data[3])
        self.planTime = int(data[4])


class Cross:
    def __init__(self):
        self.id = 0
        self.roadId1 = 0
        self.roadId2 = 0
        self.roadId3 = 0
        self.roadId4 = 0
    
    def set_info(self, data:list):
        self.id = int(data[0])
        self.roadId1 = int(data[1])
        self.roadId2 = int(data[2])
        self.roadId3 = int(data[3])
        self.roadId4 = int(data[4])   

class Road:
    def __init__(self):
        self.id  = 0
        self.length = 0
        self.speed = 0
        self.channel = 0 
        self.From = 0
        self.to = 0 
        self.isDuplex = 0

    def set_info(self, data:list):
        self.id = int(data[0])
        self. length = int(data[1])
        self.speed = int(data[2])
        self.channel = int(data[3] )
        self.From = int(data[4])
        self.to = int(data[5])
        self.isDuplex = int(data[6])


class Net:
    def __init__(self, car_path, cross_path, road_path):
        self.cars = []
        self.crosses = []
        self.roads = []
        content = []

        with open(car_path) as f:
            content = f.readlines()
        content = content[1:]
        content[-1] += '\n'
        #print(content)
        for record in content:
            c1 = Car()
            record = record[1:-2].split(',')
            #print(record)
            c1.set_info(record)
            self.cars.append(c1)
        
        with open(cross_path) as f:
            content = f.readlines()
        content = content[1:]
        content[-1] += '\n'
        for record in content:
            cr1 = Cross()
            record = record[1:-2].split(',')
            cr1.set_info(record)
            self.crosses.append(cr1)
        
        with open(road_path) as f:
            content = f.readlines()
        content = content[1:]
        content[-1] += '\n'
        for record in content:
            r = Road()
            record = record[1:-2].split(',')
            r.set_info(record)
            self.roads.append(r)
    
if __name__ == "__main__":
    car_path = "../config/car.txt"
    cross_path = "../config/cross.txt"
    road_path = "../config/road.txt"
    net = Net(car_path, cross_path, road_path)
    for ele in net.roads:
        print(ele.id)
        
