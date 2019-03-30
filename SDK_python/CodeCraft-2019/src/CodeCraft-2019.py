import logging
import sys
from hwdata.DS import  Car, Road, Cross, Net

logging.basicConfig(level=logging.DEBUG,
                    filename='../logs/CodeCraft-2019.log',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')


def main():
    if len(sys.argv) != 5:
        logging.info('please input args: car_path, road_path, cross_path, answerPath')
        exit(1)

    car_path = sys.argv[1]
    road_path = sys.argv[2]
    cross_path = sys.argv[3]
    answer_path = sys.argv[4]

    logging.info("car_path is %s" % (car_path))
    logging.info("road_path is %s" % (road_path))
    logging.info("cross_path is %s" % (cross_path))
    logging.info("answer_path is %s" % (answer_path))

    # to read input file
    # process
    # to write output file

    net = Net(car_path, road_path, cross_path)
    net.find_route()
    with open(answer_path,"w") as f:
        line = "#(carId,StartTime,RoadId...)\n"
        f.write(line)
        for answer in net.answers:
            line = "(" 
            for tos in answer:
                line += tos + ","
            line += ")\n"
            f.write(line)   
    

if __name__ == "__main__":
    main() 