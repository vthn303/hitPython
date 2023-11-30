
def readFile(filename):
    '''
    this function to read file and get value of two points
    '''
    with open(filename, 'r') as f:
        lines = f.read().split()
        a = (float(lines[1]), float(lines[2]))
        b = (float(lines[4]), float(lines[5]))
    return a, b

def distance(a, b):
    '''
    this function to solve the distance of two points
    '''
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def writeFile(filename, a, b):
    '''
    this function to write file
    '''
    with open(filename, 'w') as f:
        f.write(f"A({a[0]}, {a[1]}) B ({b[0]}, {b[1]}) AB = {round(distance(a, b), 2)}" )

a, b = readFile("input.txt")
writeFile("output.txt", a, b)