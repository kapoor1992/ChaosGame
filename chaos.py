import sys
from shapes import square
from shapes import triangle
from shapes import pentagon
from shapes import hexagon
from shapes import star
from shapes import bowtie

def parse_input(args):
    shape = args[1]
    halves = int(args[2])
    unique = args[3]

    if not((shape == 'triangle' or shape == 'square' or shape == 'pentagon' or shape == 'hexagon' or shape == 'star' or shape == 'bowtie') and
           (halves >= 1) and
           (unique == 'yes' or unique == 'no')):
           print ("To use this program: python chaos.py <shape, triangle/square/pentagon/hexagon/star/bowtie> <halves, int> <no repeats, yes/no>")
           sys.exit()
    
    if (unique == 'yes'):
        unique = True
    else:
        unique = False

    return shape, halves, unique

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
    if (shape == 'star'):
        shape = star.Star(points, refresh, halves, unique)
        shape.draw()
    if (shape == 'bowtie'):
        shape = bowtie.Bowtie(points, refresh, halves, unique)
        shape.draw()

def main():
    args = sys.argv
    points = 25000
    refresh = 5000
    
    try:
        shape, halves, unique = parse_input(args)
        make_pattern(shape, points, refresh, halves, unique)
    except Exception, e:
        print str(e)

if __name__ == '__main__':
    main()
