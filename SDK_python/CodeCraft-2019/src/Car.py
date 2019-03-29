
CarList = []  # type:List[CarInst]
__CarListIndexing = {}  # type:Dict[Int,CarInst]


class CarInst:
    def __init__(self, Id, From, to, speed, planTime):
        self.id = Id
        self.From = From
        self.to = to
        self.speed = speed
        self.planTime = planTime


def addCar(car: CarInst):
    CarList.append(car)
    __CarListIndexing[car.id] = car


def getCar(carId: int):
    # find Car in O(1)
    return __CarListIndexing.get(carId)
