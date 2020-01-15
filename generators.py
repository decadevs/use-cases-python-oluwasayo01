# Document at least 3 use cases of generators
import os
file_loc = os.path.join(os.getcwd(), 'file.txt')


def read_csv(filename):
    with open(filename) as file:
        line = file.readline()
        while line:
            line = file.readline()
            yield line
        
            

def one_billion_looper():
    for number in range(1000000000):
        yield number

