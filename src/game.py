import pygame

from const import *


class Game:

    def __int__(self):
        pass

    # Show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)  # lidth green
                    # color = (0, 0, 0)  # it's for back color
                else:
                    color = (119, 154, 88)  # dark green
                    # color + (255, 255, 255) it's for white color

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)