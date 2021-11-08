"""
PyGame tutorial: Keyboard events
https://realpython.com/pygame-a-primer/

"""

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from typing import Callable


def run_until_quit(func: Callable = lambda: None):
  running = True
  while running:
    for ev in pygame.event.get():
      if (ev.type == QUIT or
          (ev.type == KEYDOWN and ev.key == K_ESCAPE)):
        running = False
    func()


if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode([500, 500])
  run_until_quit()
