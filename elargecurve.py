import math
import random
import xy


rules = [
    {
        "a": 'L',
        "b": '+RR-L-L+R+RL+R-LR+L-R-L+RLL-R-LRLRL+R-LRLR+L+RRLRL+R-LRL-L-RL+R-LRLRL+R+RLRLRL+R-LL-R-L+RLL-R-LR+R+L-L-R+R+LL-R-LR+R+L-L-R+R+LL'
    },
    {
        "a": 'R',
        "b" : 'RR-L-L+R+R-L-LR+L+RR-L-L+R+R-L-LR+L+RRL-R+L+RR+L-RLRLRL-L-RLRLR+L-RL+R+RLR+L-RLRLL-R-LRLR+L-RLRLR+L+RRL-R+L+R-LR+L-RL-L-R+R+LL-'
        #"b": '-LL+R+R-L-LR-L+RL-R+L+R-LRR+L+RLRLR-L+RLRL-R-LLRLR-L+RLR+R+LR-L+RLRLR-L-LRLRLR-L+RR+L+R-LRR+L+RL-L-R+R+L-L-RR+L+RL-L-R+R+L-L-RR'
        #"b" : 'RR-L-L+R+RL+R-LR+L-R-L+RLL-R-LRLRL+R-LRLR+L+RRLRL+R-LLR-L-RL+R-LRLRL+R+LRLRLR+R-LL-R-L+RLL-R-LR+R+L-L-L+R+LL-R-LR+R+L-L-R+R+LL+'
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
    angle = 90
    iterations = 2
    step = 50/iterations
    #build up the rule
    for x in range(0, iterations):
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
    drawing.render().write_to_png('elargecurve.png')
    xy.draw(drawing)


if __name__ == '__main__':
    main()
