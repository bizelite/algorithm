from graphics import *


def main():
    win = GraphWin('Click me!')
    for i in range(10):
        p = win.getMouse()
        print('Your clicked at:', p.getX(), p.getY())


if __name__ == '__main__':
    main()
