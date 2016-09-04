import math
import random
import xy

def hexLattice(width, height, scale):
    forcePositions = []
    hexCentres = []
    s = scale;
    a = (3**0.5) * s / 2
    cols = math.floor(width/a/2)
    rows = math.floor((height / s/ * 2) + 1)

    idx = 0;

    for i in range(0, rows):
        for j in range(0, cols):
            centre = [
                (i % 2) * a + 2 * j * a,
                i * ((3 * s) / 2)
            ]

            pos1 = [
                centre[0],
                centre[1] + s
            ]

            hexCentres[j + i * cols] = centre

            forcePositions[idx] = pos1

            if (i % 2 == 0):
                pos2 = [
                    centre[0] - a,
                    centre[1] + s / 2
                ]
            else:
                pos2 = [
                    centre[0] + a,
                    centre[1] + s / 2
                ]

            forcePositions[idx + 1] = pos2

