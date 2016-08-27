import xy
import re
from xml.dom import minidom

def main():
    svgFile = minidom.parse('leaf.svg')
    print(svgFile);
    path_elements = svgFile.getElementsByTagName('path');
    print(path_elements);
    paths = []
    for path in path_elements:
        d = path.getAttribute('d')
        paths.extend(xy.parse_svg_path(d))
    drawing = xy.Drawing(paths).scale(1, -1).scale_to_fit(9 * 25.4, 12 * 25.4)
    im = drawing.render()
    im.write_to_png('svg.png')
    #xy.draw(drawing)

if __name__ == '__main__':
    main()
