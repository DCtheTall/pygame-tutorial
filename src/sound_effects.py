"""
PyGame tutorial: Adding sound effects
https://realpython.com/pygame-a-primer/

"""

import pygame
from pygame.constants import K_UP, K_DOWN
from typing import Sequence

from background_images import ADDSTAR, STAR_INTERVAL_MS
from draw_surface import SCREEN_WIDTH, SCREEN_HEIGHT
from enemies import ADDENEMY, ENEMY_INTERVAL_MS
from game_speed import GameLoop as GameLoopBase
from sprite_images import Player as PlayerBase, Enemy


MUSIC_MP3_PATH = 'static/Electric.mp3'
THRUSTER_WAV_PATH = 'static/thruster.wav'
COLLISION_WAV_PATH = 'static/explosion.wav'


def play_music(mp3_path=MUSIC_MP3_PATH):
  pygame.mixer.music.load(mp3_path)
  pygame.mixer.music.play(loops=-1)


class Player(PlayerBase):
  def __init__(self, sound_effect):
    super(Player, self).__init__()
    self.sound_effect = sound_effect

  def update(self, pressed_keys: Sequence[bool]):
    super().update(pressed_keys)
    if pressed_keys[K_UP] or pressed_keys[K_DOWN]:
      self.sound_effect.play()


class GameLoop(GameLoopBase):
  def __init__(self, *args):
    super(GameLoop, self).__init__(*args)
    self.collision_sound = pygame.mixer.Sound(COLLISION_WAV_PATH)

  def on_game_over(self):
    self.collision_sound.play()
    super().on_game_over()


if __name__ == '__main__':
  pygame.mixer.init()
  pygame.init()
  pygame.time.set_timer(ADDENEMY, ENEMY_INTERVAL_MS)
  pygame.time.set_timer(ADDSTAR, STAR_INTERVAL_MS)
  screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
  thruster_sound_effect = pygame.mixer.Sound(THRUSTER_WAV_PATH)
  player = Player(thruster_sound_effect)
  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)
  enemies = pygame.sprite.Group()
  game_loop = GameLoop(screen, player, enemies, all_sprites)
  game_loop.enemy_cls = Enemy

  play_music()
  game_loop.run()

  thruster_sound_effect.stop()
  pygame.mixer.music.stop()
  pygame.mixer.quit()
