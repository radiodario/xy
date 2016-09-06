import math
import random
import xy


rules = [
    {
        "a": 'F',
        "b": 'FF+[+F-F-F]-[-F+F+F]'
    }
]

axiom = "F"


def generate(sentence):
    nextSentence = ''
    for x in sentence:
        found = False
        for rule in rules:
            if rule['a'] == x:
                found = True
                nextSentence += rule['b']
                break;
        if not found:
            nextSentence += x
    return nextSentence;


def main():
    sentence = axiom
    turtle = xy.Turtle()
    angle = 25
    iterations = 1
    step = 50/iterations
    #build up the rule
    for x in range(iterations):
        sentence = generate(sentence)
    lastPos = []
    lastHead = []
    for x in sentence:
        if (x == 'F'):
            turtle.pd()
            turtle.forward(step)
        if (x == '+'):
            turtle.rt(angle)
        if (x == '-'):
            turtle.lt(angle)
        if (x == '['):
            lastPos.append(turtle.pos())
            lastHead.append(turtle.heading())
        if (x == ']'):
            turtle.pu()
            pos = lastPos.pop()
            head = lastHead.pop()
            turtle.goto(*pos)
            turtle.seth(head)


    drawing = turtle.drawing
    drawing = drawing.rotate(90)
    drawing = drawing.translate(175, 0 )
    #drawing = drawing.scale(1, -1)
    #drawing = drawing.origin()
    drawing.render().write_to_png('lsystem.png')
    xy.draw(drawing)


if __name__ == '__main__':
    main()
