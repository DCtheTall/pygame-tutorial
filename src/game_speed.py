"""
PyGame tutorial: Adding sprite images to entitiess
https://realpython.com/pygame-a-primer/

"""

import pygame

from background_images import (
  ADDSTAR,
  STAR_INTERVAL_MS,
  GameLoop as GameLoopBase,
)
from draw_surface import SCREEN_WIDTH, SCREEN_HEIGHT
from enemies import ADDENEMY, ENEMY_INTERVAL_MS
from sprite_images import Player, Enemy


FRAME_RATE = 30


class GameLoop(GameLoopBase):
  def __init__(self, *args):
    super(GameLoop, self).__init__(*args)
    self.clock = pygame.time.Clock()

  def draw_all_sprites(self):
    super().draw_all_sprites()
    self.clock.tick(FRAME_RATE)


if __name__ == '__main__':
  pygame.init()
  pygame.time.set_timer(ADDENEMY, ENEMY_INTERVAL_MS)
  pygame.time.set_timer(ADDSTAR, STAR_INTERVAL_MS)
  screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
  player = Player()
  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)
  enemies = pygame.sprite.Group()
  game_loop = GameLoop(screen, player, enemies, all_sprites)
  game_loop.enemy_cls = Enemy
  game_loop.run()
