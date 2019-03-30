import hwdata.Road as rd
import hwdata.Cross as cr
import hwdata.Car as ca

def HWDijkstra(src,tar):
    """Dijkstra Algorithm on hwdata """
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

def HWDijkstra_second_shortest(src, tar, next_hop):
    nodes = [c.id for c in cr.CrossList if c.id != next_hop]
    graph = {}
    origin_graph = {}
    for r in rd.RoadList:
        if r.From  == next_hop or r.to == next_hop:
            continue
        else:
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

if __name__ == "__main__":
    car_path = "../config/car.txt"
    cross_path = "../config/cross.txt"
    road_path = "../config/road.txt"
    net = Net(car_path, cross_path, road_path)
    net.find_route()
    print(net.answers)
