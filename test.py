import csv  
import pandas
import numpy

def calculate_distance(lat1, lat2, long1, long2):
    print('signal of x1: ' + str(numpy.sign(lat1)))
    print('signal of x2: ' + str(numpy.sign(lat2)))
    print('signal of y1: ' + str(numpy.sign(long1)))
    print('signal of y2: ' + str(numpy.sign(long2)))
   
def main():

    data = pandas.read_csv('villes.csv')
    data = data.drop(data.columns[[1, 2, 3, 4, 7]], axis = 1)
    data = data.transpose()
    data = data.to_dict()
    print(data)

    calculate_distance(-1, 1, 0, -2)


if __name__ == '__main__':
    main()