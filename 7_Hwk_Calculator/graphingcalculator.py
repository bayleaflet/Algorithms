# BJC, Original Author
# 10/2023
# Graphing Calculator. Prompts Users, must have pygame.
import pygame
import math
import sys
from stack import Stack
from InfixtoPostfix import *

def PrintInstructions():
    print("This program emulates a graphing calculator.")
    print("Valid operators include +, -, *, /, and ().")
    print("Only single digits are allowed. If you wish to include a longer digit")
    print("number, it must be derived. i.e: 28 -> (4*7).")
    print("Also, when typing in x, it must be lowercase!")


def draw_axis_marks(win, centerX, centerY, xWinHigh, yWinHigh):
    # Draw marks on the x-axis
    for i in range(-10, 11):
        mark_x = centerX + i * (xWinHigh / 20)
        pygame.draw.line(win, (0, 0, 0), (mark_x, centerY - 5), (mark_x, centerY + 5), 2)

    # Draw marks on the y-axis
    for i in range(-10, 11):
        mark_y = centerY + i * (yWinHigh / 20)
        pygame.draw.line(win, (0, 0, 0), (centerX - 5, mark_y), (centerX + 5, mark_y), 2)

def main():
    PrintInstructions()
    # Initializing pygame window
    pygame.init()

    # Define screen dimensions and coordinates
    xWinLow, yWinLow = 0, 0
    xWinHigh, yWinHigh = 500, 500

    # Create window
    win = pygame.display.set_mode((xWinHigh, yWinHigh))

    # Set Coordinates
    infix = input("Enter the function you wish to graph (e.g., x*x): ")
    xlow, ylow = -10, -10
    xhigh, yhigh = 10, 10
    incr = 0.1

    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        win.fill((255, 255, 255))  # Fill the background with white (R, G, B)

        # Calculate the center of the screen
        centerX = xWinHigh / 2
        centerY = yWinHigh / 2

        # Draw the x-axis (black)
        pygame.draw.line(win, (0, 0, 0), (0, centerY), (xWinHigh, centerY), 2)

        # Draw the y-axis (black)
        pygame.draw.line(win, (0, 0, 0), (centerX, 0), (centerX, yWinHigh), 2)

        draw_axis_marks(win, centerX, centerY, xWinHigh, yWinHigh)

        # Start implementing stack...


        pts = []

        x = xlow
        # In class way
        while x <= xhigh:
            postfix = InfixtoPostfix(infix)
            y = EvaluatePostFix(postfix,x)
            screen_x = x * (xWinHigh / (xhigh - xlow)) + centerX
            screen_y = -y * (yWinHigh / (yhigh - ylow)) + centerY
            pts.append([screen_x, screen_y])
            x += float(incr)



        # Entry1 = Entry(point(-7,-8),4) Makes entry boxes.
        # Consider adding entry boxes
        for i in range(len(pts) - 1):
            x1, y1 = pts[i]
            x2, y2 = pts[i + 1]
            pygame.draw.line(win, (245, 40, 145), (x1, y1), (x2, y2), 2)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
