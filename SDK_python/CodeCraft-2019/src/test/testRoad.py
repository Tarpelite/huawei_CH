import unittest
import hwdata.Road as rd
import hwdata.Cross  as cr
from test.CommonSetup import SetUp as su


class testRoad(unittest.TestCase):

    def testRoadRelation(self):
    #(5000, 10, 5, 1, 1, 2, 1)
    #(5001, 10, 5, 1, 2, 3, 1)
    #(1, 5000, 5005, -1, -1)
    #(2, 5001, 5006, 5000, -1)
        su()
        r1=rd.getRoad(5000)
        r2=rd.getRoad(5001)
        self.assertEqual(r1 % r2,rd.RoadInst.STRAIGHT)








