from math import sin, cos, pi, hypot, radians, sqrt
import random
import time
import xy

def circle(cx, cy, r, n):
    result = []
    for i in range(n + 1):
        p = i / float(n)
        a = 2 * pi * p
        x = cx + cos(a) * r
        y = cy + sin(a) * r
        result.append((x, y))
    return result

def main():
    c = 2;

    paths = []
    for n in range(0, 2500):
        a = n * radians(137.5);
        r = c * sqrt(n)
        x = r * cos(a)
        y = r * sin(a)
        paths.append(circle(x, y, 0.75, 32));

    drawing = xy.Drawing(paths)
    drawing = drawing.rotate_and_scale_to_fit(255, 380, step=90).origin()
    drawing = drawing.sort_paths_greedy()
    im = drawing.render()
    im.write_to_png('phylotaxis.png')
    xy.draw(drawing)

if __name__ == '__main__':
    main()
