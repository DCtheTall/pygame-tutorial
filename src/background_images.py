"""
PyGame tutorial: Adding background images
https://realpython.com/pygame-a-primer/

"""

import pygame
import random
from pygame.locals import RLEACCEL

from draw_surface import SCREEN_WIDTH, SCREEN_HEIGHT
from enemies import ADDENEMY, ENEMY_INTERVAL_MS, GameLoop as GameLoopBase
from sprite_images import Player, Enemy
from user_input import Entity


ADDSTAR = ADDENEMY + 1
STAR_INTERVAL_MS = 2 * ENEMY_INTERVAL_MS
STAR_SPRITE_PATH = 'static/star.jpg'


class Star(Entity):
  def __init__(self):
    super(Star, self).__init__()
    self.surface = pygame.image.load(STAR_SPRITE_PATH).convert()
    self.surface.set_colorkey((0, 0, 0), RLEACCEL)
    self.rect = self.surface.get_rect(
        center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)))
  
  def update(self, *_):
    self.rect.move_ip(-5, 0)
    if self.rect.right < 0:
      self.kill()


class GameLoop(GameLoopBase):
  def on_event(self, ev: pygame.event.Event):
    super().on_event(ev)
    if ev.type == ADDSTAR:
      star = Star()
      self.all_sprites.add(star)
      


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
