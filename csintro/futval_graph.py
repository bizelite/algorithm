from graphics import *

def main():

    # A Guide Message
    print('This program plots the growth of a 10-year investment.')


    # Input principal and interest rate
    principal = float(input('Enter the initial principal: '))
    apr = float(input('Enter the annualized interest rate: '))
    
    # Set graphics window on left-side with label
    win = GraphWin('Investment Growth Chart', 320, 240)
    win.setBackground('white')
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    # Draw bar-graph about initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

    # Draw bar-graph about next years
    for year in range(1, 11):
        # Calculate investment value next year
        principal = principal * (1 + apr)
        # Draw bar-graph about calculated value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)

    input('Press <Enter> to quit')
    win.close()

if __name__ == '__main__':
    main()