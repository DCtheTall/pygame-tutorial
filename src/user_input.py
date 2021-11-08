"""
PyGame tutorial: Processing user input
https://realpython.com/pygame-a-primer/

"""

import pygame
from pygame.locals import (
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_UP,
)
from typing import Sequence

from draw_surface import SCREEN_WIDTH, SCREEN_HEIGHT
from keyboard_events import run_until_quit
from player import draw_player


KEYS_TO_DIRECTIONS = {
  K_DOWN:  (0, 1),
  K_LEFT:  (-1, 0),
  K_RIGHT: (1, 0),
  K_UP:    (0, -1),
}
SPEED = 5


class Entity(pygame.sprite.Sprite):
  surface: pygame.Surface
  rect: pygame.Rect


class Player(Entity):
  def __init__(self):
    super(Player, self).__init__()
    self.surface = surface = pygame.Surface((75, 25))
    surface.fill((255, 255, 255))
    self.rect = surface.get_rect()

  def update(self, pressed_keys: Sequence[bool]):
    for key, (x, y) in KEYS_TO_DIRECTIONS.items():
      if pressed_keys[key]:
        self.rect.move_ip(SPEED * x, SPEED * y)

    # Stay in bounds
    self.rect.left = max(0, self.rect.left)
    self.rect.right = min(SCREEN_WIDTH, self.rect.right)
    self.rect.top = max(0, self.rect.top)
    self.rect.bottom = min(SCREEN_HEIGHT, self.rect.bottom)


def draw_player(screen: pygame.Surface, player: Player):
  """Draw the player sprite."""
  screen.fill((0, 0, 0))
  screen.blit(player.surface, player.rect)
  pygame.display.flip()


def update(screen: pygame.Surface, player: Player):
  player.update(pygame.key.get_pressed())
  draw_player(screen, player)


if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
  player = Player()
  run_until_quit(lambda: update(screen, player))
