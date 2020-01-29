import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
import csv
if __name__ == '__main__':

    file = sys.stdin.readlines()

    for line in csv.reader(file):
        key = line[0]
        value = line[1]

        sys.stdout.write("{},{}\n".format(value,key))
