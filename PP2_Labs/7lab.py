# # 1)
# import pygame
# import os
# import time
# from datetime import datetime

# _image_library = {}
# def get_image(path):
#         global _image_library
#         image = _image_library.get(path)
#         if image == None:
#                 canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
#                 image = pygame.image.load(canonicalized_path)
#                 _image_library[path] = image
#         return image

# pygame.init()
# screen = pygame.display.set_mode((800,600))
# done = False
# clock = pygame.time.Clock()
# original_rect = get_image('min_hand.png').get_rect()
# center = original_rect.center

# min_offset = 45
# sec_offset = -60

# while not done:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       done = True
      
#   screen.fill((255, 255, 255))
#   screen.blit(get_image('clock.png'), (0, 0))
  
#   now = datetime.now()
#   sec = now.second
#   minutes = now.minute
#   angle_sec = - (sec * 6 + sec_offset)
#   angle_min = - (minutes * 6 + min_offset)
  
  
#   rotated_min = pygame.transform.rotate(get_image('min_hand.png'), angle_min)
#   rotated_sec = pygame.transform.rotate(get_image('sec_hand.png'), angle_sec)
#   rotated_m = rotated_min.get_rect(center=original_rect.center)
#   rotated_s = rotated_sec.get_rect(center=original_rect.center)

#   screen.blit(rotated_min, rotated_m)
#   screen.blit(rotated_sec, rotated_s)
  
#   pygame.display.flip()
#   clock.tick(1)

# # 2)
# import pygame

# playlist = [r"C:\Users\Victus\Desktop\Ali\Python\Pygame\kajjrat-nurtas-njusha-almaty-tunderi.mp3", r"Кайрат Нуртас, ИРИНА КАЙРАТОВНА - Тун-[muzmir.kz].mp3"]
# current_track = 0

# def play():
#   pygame.mixer.music.load(playlist[current_track])
#   pygame.mixer.music.play(-1)
#   print(f"Playing")
  
# def stop():
#   pygame.mixer.music.stop()
#   print("Music stopped")

# def next():
#   global current_track
#   current_track = (current_track + 1) % len(playlist)
#   play()

# def previous():
#   global current_track
#   current_track = (current_track - 1) % len(playlist)
#   play()

# pygame.init()
# done = False
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((200, 200))

# while not done:
#   clock.tick(60)
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       done = True

#   screen.fill((255, 255, 255))
#   pressed = pygame.key.get_pressed() 
#   if pressed[pygame.K_SPACE]: stop() #stop
#   if pressed[pygame.K_0]: play() #play
#   if pressed[pygame.K_RIGHT]: next() #next
#   if pressed[pygame.K_LEFT]: previous() #previous

#   pygame.display.flip()

# 3)
import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Controller")

BALL_RADIUS = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
BALL_COLOR = (255, 0, 0)
BG_COLOR = (255, 255, 255)
MOVE_STEP = 20

running = True
while running:
  clock.tick(60)  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP] and ball_y - BALL_RADIUS - MOVE_STEP >= 0:
    ball_y -= MOVE_STEP
  if pressed[pygame.K_DOWN] and ball_y + BALL_RADIUS + MOVE_STEP <= HEIGHT:
    ball_y += MOVE_STEP
  if pressed[pygame.K_LEFT] and ball_x - BALL_RADIUS - MOVE_STEP >= 0:
    ball_x -= MOVE_STEP
  if pressed[pygame.K_RIGHT] and ball_x + BALL_RADIUS + MOVE_STEP <= WIDTH:
    ball_x += MOVE_STEP
  
  screen.fill(BG_COLOR)
  pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
  pygame.display.flip()

pygame.quit()