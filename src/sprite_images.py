"""
PyGame tutorial: Adding sprite images to entitiess
https://realpython.com/pygame-a-primer/

"""

import pygame
import random
from pygame.locals import RLEACCEL

from draw_surface import SCREEN_WIDTH, SCREEN_HEIGHT
from user_input import Player as PlayerBase
from enemies import (
  ADDENEMY,
  ENEMY_INTERVAL_MS,
  GameLoop,
  Enemy as EnemyBase,
)


SHIP_SPRITE_PATH = 'static/ship.jpg'
ENEMY_SPRITE_PATH = 'static/enemy.jpg'


class Player(PlayerBase):
  def __init__(self):
    super(Player, self).__init__()
    self.surface = pygame.image.load(SHIP_SPRITE_PATH).convert()
    self.surface.set_colorkey((255, 255, 255), RLEACCEL)
    self.rect = self.surface.get_rect()


class Enemy(EnemyBase):
  def __init__(self):
    super(Enemy, self).__init__()
    self.surface = pygame.image.load(ENEMY_SPRITE_PATH).convert()
    self.surface.set_colorkey((255, 255, 255), RLEACCEL)
    self.rect = self.surface.get_rect()
    self.rect = self.surface.get_rect(
        center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)))
    self.speed = random.randint(5, 20)


if __name__ == '__main__':
  pygame.init()
  # Emits this event every 250ms
  pygame.time.set_timer(ADDENEMY, ENEMY_INTERVAL_MS)
  screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
  player = Player()
  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)
  enemies = pygame.sprite.Group()
  game_loop = GameLoop(screen, player, enemies, all_sprites)
  game_loop.enemy_cls = Enemy
  game_loop.run()
