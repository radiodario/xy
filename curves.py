import math
import random
import xy


rules = [
    {
        "a": 'L',
        "b": 'L+R++R-L--LL-R+'
    },
    {
        "a" : 'R',
        "b" : '-L+RR++R+L--L-R'
    }
]



axiom = "L"


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
    angle = 60
    iterations = 5
    step = 50/iterations
    #build up the rule
    for x in range(iterations):
        sentence = generate(sentence)
    lastPos = []
    lastHead = []
    for x in sentence:
        if (x == 'L'):
            turtle.forward(step)
        if (x == 'R'):
            turtle.forward(step)
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
    drawing = drawing.rotate_and_scale_to_fit(275, 380, step=90)
    #drawing = drawing.scale(1, -1)
    drawing = drawing.origin()
    drawing.render().write_to_png('curves.png')
    #xy.draw(drawing)


if __name__ == '__main__':
    main()
