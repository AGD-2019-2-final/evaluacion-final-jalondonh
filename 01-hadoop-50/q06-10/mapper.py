import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<

for line in sys.stdin:
    line = line.strip()
    line = line.split('  ')
    letter = line[0]
    number = line[2]
    
    sys.stdout.write("{},{}\n".format(letter, number))

