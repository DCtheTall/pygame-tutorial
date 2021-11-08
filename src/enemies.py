"""
PyGame tutorial: Adding enemies to a game
https://realpython.com/pygame-a-primer/

"""

import pygame
import random
from pygame.locals import (
  K_ESCAPE,
  KEYDOWN,
  QUIT,
)

from draw_surface import SCREEN_WIDTH, SCREEN_HEIGHT
from user_input import Entity, Player


ADDENEMY = pygame.USEREVENT + 1
ENEMY_COLOR = (255, 10, 10)
ENEMY_INTERVAL_MS = 250


class Enemy(Entity):
  def __init__(self):
    super(Enemy, self).__init__()
    self.surface = surface = pygame.Surface((20, 10))
    surface.fill(ENEMY_COLOR)
    self.rect = surface.get_rect(
        center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)))
    self.speed = random.randint(5, 20)

  def update(self, *_):
    self.rect.move_ip(-self.speed, 0)
    if self.rect.right < 0:
      self.kill()


class GameLoop:
  def __init__(self,
               screen: pygame.Surface,
               player: Player,
               enemies: pygame.sprite.Group,
               all_sprites: pygame.sprite.Group):
    self.screen = screen
    self.player = player
    self.enemies = enemies
    self.all_sprites = all_sprites
    self.running = False
    self.enemy_cls = Enemy

  def run(self):
    self.running = True
    while self.running:
      for ev in pygame.event.get():
        if (ev.type == QUIT or
             (ev.type == KEYDOWN and ev.key == K_ESCAPE)):
          self.on_game_over()
        else:
          self.on_event(ev)
      self.update()

  def on_event(self, ev: pygame.event.Event):
    if ev.type == ADDENEMY:
      enemy = self.enemy_cls()
      self.enemies.add(enemy)
      self.all_sprites.add(enemy)

  def update(self):
    keys_pressed = pygame.key.get_pressed()
    for entity in self.all_sprites:
      entity.update(keys_pressed)
    if pygame.sprite.spritecollide(self.player, self.enemies, True):
      self.on_game_over()
    self.draw_all_sprites()

  def on_game_over(self):
    self.running = False

  def draw_all_sprites(self):
    """Draw the player sprite."""
    self.screen.fill((0, 0, 0))
    for entity in self.all_sprites:
      self.screen.blit(entity.surface, entity.rect)
    pygame.display.flip()


if __name__ == '__main__':
  pygame.init()
  pygame.time.set_timer(ADDENEMY, ENEMY_INTERVAL_MS)
  screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
  player = Player()
  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)
  enemies = pygame.sprite.Group()
  GameLoop(screen, player, enemies, all_sprites).run()
