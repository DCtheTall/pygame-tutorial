"""
PyGame tutorial: Creating a player sprite
https://realpython.com/pygame-a-primer/

"""

import pygame

from draw_surface import SCREEN_WIDTH, SCREEN_HEIGHT
from keyboard_events import run_until_quit


class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surface = surface = pygame.Surface((75, 25))
    surface.fill((255, 255, 255))
    self.rect = surface.get_rect()


def draw_player(screen: pygame.Surface, player: Player):
  """Draw the player sprite."""
  screen.fill((0, 0, 0))
  screen.blit(player.surface, (SCREEN_WIDTH >> 1, SCREEN_HEIGHT >> 1))
  pygame.display.flip()


if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
  player = Player()
  run_until_quit(lambda: draw_player(screen, player))
