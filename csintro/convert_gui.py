from graphics import *


def main():
    win = GraphWin('Celsius Converter', 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1, 3), ' Celsius Temperature: ').draw(win)
    Text(Point(1, 1), 'Fahrenheit Temperature: ').draw(win)
    inputText = Entery(Point(2.23, 3), 5)
    inputText.setText('0.0')
    inputText.draw(win)
