import xy
import random
from poisson_disc import poisson_disc

max_dist = 50
min_dist = 5

def distance((x1, y1), (x2, y2)):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def magnitude(p1):
    return distance((0, 0), p1)

def add((x1, y1), (x2, y2)):
    return (x1+x2, y1+y2)

def sub(p1, (x2, y2)):
    return add(p1, (-x2, -y2))

def norm((x, y)):
    m = magnitude((x,y))
    return (x/m, y/m)

def mult((x, y), n):
    return (x*n, y*n)

def div((x, y), n):
    return (x/n, y/n)

class Leaf():
    def __init__(self, pos):
        self.pos = pos
        self.reached = False
    def draw(self):
        return xy.circle(self.pos[0], self.pos[1], 1, 32)

class Branch():
    def __init__(self, pos, direction, parent):
        self.pos = pos
        self.direction = direction
        self.originalDirection = direction
        self.length = 3;
        self.parent = parent
        self.count = 0
        return

    def reset(self):
        self.direction = self.originalDirection
        self.count = 0

    def next(self):
        scaledDirection = mult(self.direction, self.length)
        return Branch(add(self.pos, scaledDirection), self.direction, self)

    def draw(self):
        if not self.parent:
            return [self.pos, self.pos]
        return [self.parent.pos, self.pos]

class Tree():
    def __init__(self, numLeaves, w, h):
        self.leaves = []
        self.branches = []

        print "generating leaves"
        points, paths = poisson_disc(0, 0, w, w, 2, 1)
        for pos in points:
            self.leaves.append(Leaf(pos))

        print "building branches"
        root = Branch((w/2, h), (0, -1), None)
        self.branches.append(root)

        current = root;
        found = False

        while not found:
            for leaf in self.leaves:
                d = distance(current.pos, leaf.pos)
                if (d < max_dist):
                    found = True
            if not found:
                branch = current.next()
                current = branch
                self.branches.append(branch)

    def grow(self):
        print "\t leaves:"
        for leaf in self.leaves:
            closest = None
            record = 10000000;
            for branch in self.branches:
                d = distance(leaf.pos, branch.pos)
                if d < min_dist:
                    leaf.reached = True
                    closest = None
                    break
                elif d > max_dist:
                    continue
                elif closest is None or d < record:
                    closest = branch
                    record = d
            if closest is not None:
                closest.count += 1
                newDirection = norm(sub(leaf.pos, closest.pos))
                closest.direction = add(closest.direction, newDirection)

        for i in xrange(len(self.leaves) -1, 0, -1):
            if self.leaves[i].reached:
                del self.leaves[i]
        print "\t\t" + str(len(self.leaves)) + " left"

        for i in xrange(len(self.branches) -1, 0, -1):
            branch = self.branches[i]
            if branch.count > 0:
                branch.direction = div(branch.direction, branch.count)
                self.branches.append(branch.next())
            branch.reset()


    def draw(self):
        paths = []
        for leaf in self.leaves:
            paths.append(leaf.draw())
        for branch in self.branches:
            paths.append(branch.draw())
        return xy.Drawing(paths)



def main():
    try:
        drawing = xy.Drawing.load('tree_colonisation.dwg')
    except Exception:
        tree = Tree(1000, 275, 350)
        for i in range(100):
            print "growth iteration " + str(i)
            tree.grow()
        drawing = tree.draw()
        drawing.save('tree_colonisation.dwg')
    drawing = drawing.rotate_and_scale_to_fit(275, 380, step=90).scale(1, -1).origin()
    drawing = drawing.simplify_paths()
    drawing = drawing.sort_paths_greedy()
    drawing = drawing.join_paths()
    drawing = drawing.remove_duplicates()
    drawing.render().write_to_png('tree_colonisation.png')
    xy.draw(drawing)


if __name__ == '__main__':
    main()
