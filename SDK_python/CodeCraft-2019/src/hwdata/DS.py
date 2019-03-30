import RoadInst as rd
import CrossInst as cr
import CarInst as ca
import functools

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

        

    def my_dijkstra(self, src, tar):
        nodes  = [c.id for c in cr.CrossList]
        graph = {}
        origin_graph = {}
        for r in rd.RoadList:
            ed = (r.From, r.to)
            origin_graph[ed] = r.id
            graph[ed] = r.length
            if r.isDuplex:
                ed = (r.to, r.From)
                origin_graph[ed] = r.id
                graph[ed] = r.length
        visited = []
        if src in nodes:
            visited.append(src)
            nodes.remove(src)
        else:
            return None
        
        distance = {src:0}
        for i in nodes:
            query = (src, i)
            if src == i:
                distance[i] = 0
            elif not graph.get(query):
                distance[i] = float('inf')
            else:
                distance[i] = graph.get(query)
        
        path = {src:{src:[]}}
        k = pre = src
        while nodes:
            mid_distance = float('inf')
            for v in visited:
                for d in nodes:
                    q1 = (src, v)
                    q2 = (v, d)
                    if src == v:
                        a1 = 0
                    elif not graph.get(q1):
                        a1 = float('inf')
                    else:
                        a1 = graph.get(q1)

                    if v == d:
                        a2 = 0
                    elif not graph.get(q2):
                        a2 = float('inf')
                    else:
                        a2 = graph.get(q2)
                    
                    new_distance = a1 + a2
                    if new_distance < mid_distance:
                        mid_distance = new_distance
                        key = (src, d)
                        graph[key] = new_distance
                        k = d
                        pre = v
            distance[k] = mid_distance
            path[src][k]=[i for i in path[src][pre]]
            path[src][k].append(k)
            visited.append(k)
            nodes.remove(k)
        
        path_ex = [src]
        path_ex.extend(path[src][tar])
        path_ans = []
        for i in range(len(path_ex)-1):
            query = (path_ex[i], path_ex[i+1])
            path_ans.append(origin_graph.get(query))
        return path_ans
     
    
    def find_route(self):
        for c in ca.CarList:
            res = [c.id]
            path = self.my_dijkstra( c.From, c.to)
            res.extend(path)
            self.answers.append(res)
    
if __name__ == "__main__":
    car_path = "/home/tarpe/酋长的工作区/huawei_softChallenge/huawei_CH/SDK_python/CodeCraft-2019/config/car.txt"
    cross_path = "/home/tarpe/酋长的工作区/huawei_softChallenge/huawei_CH/SDK_python/CodeCraft-2019/config/cross.txt"
    road_path = "/home/tarpe/酋长的工作区/huawei_softChallenge/huawei_CH/SDK_python/CodeCraft-2019/config/road.txt"
    net = Net(car_path, cross_path, road_path)
    net.find_route()
    print(net.answers)
        