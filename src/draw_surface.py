"""
PyGame tutorial: Drawing on the screen
https://realpython.com/pygame-a-primer/

"""

import pygame

from keyboard_events import run_until_quit


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_surface(screen: pygame.Surface, surface: pygame.Surface):
  """Draw the surface in the center of the screen."""
  screen.fill((255, 255, 255))
  surface.fill((0, 0, 0))
  # rect = surface.get_rect()
  w = (SCREEN_WIDTH - surface.get_width()) >> 1
  h = (SCREEN_HEIGHT - surface.get_height()) >> 1
  screen.blit(surface, (w, h))
  pygame.display.flip()


if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
  surface = pygame.Surface([50, 50])
  run_until_quit(lambda: draw_surface(screen, surface))
