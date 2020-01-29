import sys
import re

if __name__ == '__main__':
    for line in sys.stdin:

        linere = re.sub("\n","",line)
        lista = linere.split(",")

        sys.stdout.write("{},{}\n".format(lista[1],lista[0]))