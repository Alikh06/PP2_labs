# 1)
# import pygame
# import random
# import time

# pygame.init()
# pygame.mixer.init()

# clock = pygame.time.Clock()
# FPS = 60

# WIDTH = 400
# HEIGHT = 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# backgroud = pygame.image.load(r"C:\Users\Victus\Desktop\Ali\PP1\PP2_Labs\recources\AnimatedStreet.png")

# player_img = pygame.image.load(r"C:\Users\Victus\Desktop\Ali\PP1\PP2_Labs\recources\Player.png")
# enemy_img = pygame.image.load(r"C:\Users\Victus\Desktop\Ali\PP1\PP2_Labs\recources\Enemy.png")
# coin_img = pygame.image.load(r"C:\Users\Victus\Desktop\Ali\PP1\PP2_Labs\recources\coin.png")
# coin_img = pygame.transform.scale(coin_img, (55, 55))
# backgroud_music = pygame.mixer.music.load(r"C:\Users\Victus\Desktop\Ali\PP1\PP2_Labs\recources\background.wav")
# crash_sound = pygame.mixer.Sound(r"C:\Users\Victus\Desktop\Ali\PP1\PP2_Labs\recources\crash.wav")

# font = pygame.font.SysFont("Verdana", 60)
# game_over = font.render("Game Over", True, "red")

# coin_count_font = pygame.font.SysFont("Verdana", 20)
# coin_count = 0

# pygame.mixer.music.play(-1)

# PLAYER_SPEED = 5
# ENEMY_SPEED = 4

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = player_img
#         self.rect = self.image.get_rect()
#         self.rect.x = WIDTH // 2 - self.rect.w // 2
#         self.rect.y = HEIGHT - self.rect.h
        
#     def move(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.rect.move_ip(-PLAYER_SPEED, 0) # moves the rectangle, in place
#         if keys[pygame.K_RIGHT]:
#             self.rect.move_ip(PLAYER_SPEED, 0)
#         if self.rect.left < 0:
#             self.rect.left = 0
#         if self.rect.right > WIDTH:
#             self.rect.right = WIDTH
            
# class Enemy(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = enemy_img
#         self.rect = self.image.get_rect()
#         self.generate_random_rect()
        
#     def move(self):
#         self.rect.move_ip(0, ENEMY_SPEED)
#         if self.rect.top > HEIGHT:
#             self.generate_random_rect()
            
#     def generate_random_rect(self):
#         self.rect.x = random.randint(0, WIDTH - self.rect.w)
#         self.rect.y = 0
        
# class Coin(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = coin_img
#         self.rect = self.image.get_rect()
#         self.generate_random_rect()
        
#     def move(self):
#         self.rect.move_ip(0, ENEMY_SPEED // 2)
#         if self.rect.top > HEIGHT:
#             self.generate_random_rect()
            
#     def generate_random_rect(self):
#         self.rect.x = random.randint(0, WIDTH - self.rect.w )
#         self.rect.y = -self.rect.h    # Спавн за пределами экрана

        
# player = Player()
# enemy = Enemy()
# coin = Coin()

# all_sprites = pygame.sprite.Group()
# enemy_sprites = pygame.sprite.Group()
# coin_sprites = pygame.sprite.Group()

# all_sprites.add(player, enemy, coin)
# enemy_sprites.add(enemy)
# coin_sprites.add(coin)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     screen.blit(backgroud, (0, 0))

#     player.move()
#     enemy.move()
#     coin.move()
    
#     for entity in all_sprites:
#         screen.blit(entity.image, entity.rect)
    
#     # Проверяем столкновение игрока с монетой
#     if pygame.sprite.spritecollideany(player, coin_sprites):
#         coin_count += 1
#         coin.generate_random_rect()
    
#     # Проверяем столкновение игрока и врага
#     if pygame.sprite.spritecollideany(player, enemy_sprites):
#         crash_sound.play()
#         time.sleep(1)

#         screen.fill("black")
#         center_rect = game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
#         screen.blit(game_over, center_rect)

#         pygame.display.flip()

#         time.sleep(2)
#         running = False
    
#     # Отображение счёта
#     counting = coin_count_font.render(f"Coins: {coin_count}", True, "black")
#     screen.blit(counting, (10, 10))
    
#     pygame.display.flip() 
#     clock.tick(FPS)
# pygame.quit()


# 2)
import pygame
import random
from color_palette import *

pygame.init()

# Размер окна и ячейки
WIDTH, HEIGHT = 600, 600
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки (для змейки и еды)
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Класс змейки
class Snake:
  def __init__(self):
    self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
    self.dx, self.dy = 1, 0  # Направление движения
    self.grow = False  # Флаг для роста змейки

  def move(self):
    if self.grow:
      self.body.append(Point(self.body[-1].x, self.body[-1].y))
      self.grow = False
    
    # Перемещение тела змейки
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i].x = self.body[i - 1].x
      self.body[i].y = self.body[i - 1].y

    # Двигаем голову змейки
    self.body[0].x += self.dx
    self.body[0].y += self.dy

  def draw(self):
    pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
    for segment in self.body[1:]:
      pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

  def check_collision(self, food):
    if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
      self.grow = True  # Увеличиваем змейку
      return True
    return False

  def check_self_collision(self):
    head = self.body[0]
    return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

  def check_wall_collision(self):
    head = self.body[0]
    return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

# Класс еды
class Food:
  def __init__(self):
    self.randomize()

  def randomize(self):
    self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

  def draw(self):
    pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

# Отображение текста (счёт и уровень)
def draw_text(text, x, y, color):
  font = pygame.font.Font(None, 36)
  surface = font.render(text, True, color)
  screen.blit(surface, (x, y))

# Инициализация игры
FPS = 5
score = 0
level = 1
clock = pygame.time.Clock()
food = Food()
snake = Snake()

game_over = pygame.font.SysFont("Verdana", 60).render("Game Over", True, "red")

running = True
while running:
  screen.fill(colorBLACK)  # Очищаем экран
  draw_grid_chess()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT and snake.dx == 0:
        snake.dx, snake.dy = 1, 0
      elif event.key == pygame.K_LEFT and snake.dx == 0:
        snake.dx, snake.dy = -1, 0
      elif event.key == pygame.K_DOWN and snake.dy == 0:
        snake.dx, snake.dy = 0, 1
      elif event.key == pygame.K_UP and snake.dy == 0:
        snake.dx, snake.dy = 0, -1

  snake.move()
  
  # Проверка на столкновение с собой или со стеной
  if snake.check_self_collision() or snake.check_wall_collision():
    screen.fill(colorBLACK)
    center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over, center_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    running = False
    continue

  if snake.check_collision(food):
    food.randomize()
    score += 1  # Увеличиваем очки
    
    # Повышение уровня каждые 4 очка
    if score % 4 == 0:
      level += 1
      FPS += 1  # Увеличиваем скорость игры

  # Рисуем объекты
  snake.draw()
  food.draw()
  draw_text(f"Score: {score}", 10, 10, colorBLACK)
  draw_text(f"Level: {level}", 10, 40, colorBLACK)
  
  pygame.display.flip()
  clock.tick(FPS)

pygame.quit()