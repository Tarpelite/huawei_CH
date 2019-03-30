
CarList = []  # type:List[CarInst]
__CarListIndexing = {}  # type:Dict[Int,CarInst]


class CarInst:
    CAR_WAITING=0
    CAR_RUNNING=1
    CAR_STOPPED=2
    def __init__(self, Id, From, to, speed, planTime):
        self.id = Id
        self.From = From
        self.to = to
        self.speed = speed
        self.planTime = planTime
        self.status = self.CAR_WAITING










def addCar(car: CarInst):
    CarList.append(car)
    __CarListIndexing[car.id] = car


def getCar(carId: int):
    # find Car in O(1)
    return __CarListIndexing.get(carId)
