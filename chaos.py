import sys
from shapes import square
from shapes import triangle
from shapes import pentagon
from shapes import hexagon

def parse_input(args):
    shape = args[1]
    points = int(args[2])
    refresh = int(args[3])
    halves = int(args[4])
    unique = args[5]

    if not((shape == 'triangle' or shape == 'square' or shape == 'pentagon' or shape == 'hexagon') and
           (points > 1) and
           (refresh >= 1) and
           (halves >= 1) and
           (unique == 'yes' or unique == 'no')):
           print ("To use this program: python chaos.py <shape, triangle/square/pentagon/hexagon> <points, int> <refesh rate, int> <halves, int> <no repeats, yes/no>")
           sys.exit()
    
    if (unique == 'yes'):
        unique = True
    else:
        unique = False

    return shape, points, refresh, halves, unique

def make_pattern(shape, points, refresh, halves, unique):
    if (shape == 'triangle'):
        shape = triangle.Triangle(points, refresh, halves, unique)
        shape.draw()
    if (shape == 'square'):
        shape = square.Square(points, refresh, halves, unique)
        shape.draw()
    if (shape == 'pentagon'):
        shape = pentagon.Pentagon(points, refresh, halves, unique)
        shape.draw()
    if (shape == 'hexagon'):
        shape = hexagon.Hexagon(points, refresh, halves, unique)
        shape.draw()

def main():
    args = sys.argv
    
    try:
        shape, points, refresh, halves, unique = parse_input(args)
        make_pattern(shape, points, refresh, halves, unique)
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    main()
