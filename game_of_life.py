import pygame
from pygame.locals import *

WITDH = 600
HEIGHT = 600

def main():
    pygame.init()
    pygame.display.set_caption("game of life")
    screen = pygame.display.set_mode((WITDH,HEIGHT))