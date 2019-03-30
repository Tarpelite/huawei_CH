import unittest
import src.hwalgorithm.DS as DS
from src.hwalgorithm.graph import  HWDijkstra, HWDijkstra_second_shortest
import src.hwdata.Car as ca
from src.test.CommonSetup import SetUp as su

class testRoad(unittest.TestCase):

    def testRoadRelation(self):
        su()
        c1 = ca.CarList[0]
        path = HWDijkstra(c1.From, c1.to)
        print(path)
        next_hop = path[0]
        shortest_path = HWDijkstra_second_shortest(c1.From, c1.to, next_hop)
        print(shortest_path)
        self.assertEqual(path, None)