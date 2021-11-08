"""
PyGame tutorial: First sample program
https://realpython.com/pygame-a-primer/

"""

import pygame
from typing import Callable


def run_until_quit(func: Callable):
  running = True
  while running:
    for ev in pygame.event.get():
      if ev.type == pygame.QUIT:
        running = False
    func()


def draw_circle(screen: pygame.Surface):
  """Draw a blue circle in the center of the screen."""
  pygame.draw.circle(screen, [0, 0, 255], [250, 250], 75)
  pygame.display.flip()


if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode([500, 500])
  run_until_quit(lambda: draw_circle(screen))
