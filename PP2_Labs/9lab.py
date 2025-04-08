# # 1)
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
#         x = random.randint(45, 70)
#         self.image = pygame.transform.scale(self.image, (x, x)) #изменяем размер
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
    
#     if coin_count == 3:
#         ENEMY_SPEED = 6
#     elif coin_count == 6:
#         ENEMY_SPEED = 7
#     elif coin_count == 12:
#         ENEMY_SPEED = 8         #Increasing speed when player earns n coin
    
#     pygame.display.flip() 
#     clock.tick(FPS)
# pygame.quit()


# # 2)
# import pygame
# import random
# from color_palette import *

# pygame.init()

# # Размер окна и ячейки
# WIDTH, HEIGHT = 600, 600
# CELL = 30
# screen = pygame.display.set_mode((WIDTH, HEIGHT))

# def draw_grid():
#     for i in range(HEIGHT // 2):
#         for j in range(WIDTH // 2):
#             pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# def draw_grid_chess():
#     colors = [colorWHITE, colorGRAY]

#     for i in range(HEIGHT // 2):
#         for j in range(WIDTH // 2):
#             pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# # Класс точки (для змейки и еды)
# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

# # Класс змейки
# class Snake:
#   def __init__(self):
#     self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
#     self.dx, self.dy = 1, 0  # Направление движения
#     self.grow = False  # Флаг для роста змейки

#   def move(self):
#     if self.grow:
#       self.body.append(Point(self.body[-1].x, self.body[-1].y))
#       self.grow = False
    
#     # Перемещение тела змейки
#     for i in range(len(self.body) - 1, 0, -1):
#       self.body[i].x = self.body[i - 1].x
#       self.body[i].y = self.body[i - 1].y

#     # Двигаем голову змейки
#     self.body[0].x += self.dx
#     self.body[0].y += self.dy

#   def draw(self):
#     pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
#     for segment in self.body[1:]:
#       pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

#   def check_collision(self, food):
#     if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
#       self.grow = True  # Увеличиваем змейку
#       return True
#     return False

#   def check_self_collision(self):
#     head = self.body[0]
#     return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

#   def check_wall_collision(self):
#     head = self.body[0]
#     return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

# # Класс еды
# class Food:
#   def __init__(self):
#     self.food_types = [
#       {"color": colorGREEN, "weight": 70},  # Обычная еда (чаще)
#       {"color": colorBLUE, "weight": 20},   # Средняя редкость
#       {"color": colorYELLOW, "weight": 10}  # Редкая еда (реже)
#     ]
#     self.spawn_time = pygame.time.get_ticks()  # Время появления еды
#     self.lifetime = random.randint(3000, 7000)  # Живет от 3 до 7 секунд
#     self.randomize()
    

#   def randomize(self):
#     chosen_food = random.choices(self.food_types, weights=[f["weight"] for f in self.food_types])[0]
#     self.color = chosen_food["color"]
#     self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
#     self.spawn_time = pygame.time.get_ticks()  # Обновляем время появления
#     self.lifetime = random.randint(3000, 7000)  # Новое случайное время жизни

#   def is_expired(self):
#     return pygame.time.get_ticks() - self.spawn_time > self.lifetime

#   def draw(self):
#     pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    
# # Отображение текста (счёт и уровень)
# def draw_text(text, x, y, color):
#   font = pygame.font.Font(None, 36)
#   surface = font.render(text, True, color)
#   screen.blit(surface, (x, y))

# # Инициализация игры
# FPS = 5
# score = 0
# level = 1
# clock = pygame.time.Clock()
# food = Food()
# snake = Snake()

# game_over = pygame.font.SysFont("Verdana", 60).render("Game Over", True, "red")

# running = True
# while running:
#   screen.fill(colorBLACK)  # Очищаем экран
#   draw_grid_chess()
  
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       running = False
#     elif event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_RIGHT and snake.dx == 0:
#         snake.dx, snake.dy = 1, 0
#       elif event.key == pygame.K_LEFT and snake.dx == 0:
#         snake.dx, snake.dy = -1, 0
#       elif event.key == pygame.K_DOWN and snake.dy == 0:
#         snake.dx, snake.dy = 0, 1
#       elif event.key == pygame.K_UP and snake.dy == 0:
#         snake.dx, snake.dy = 0, -1

#   snake.move()
  
#   # Проверка на столкновение с собой или со стеной
#   if snake.check_self_collision() or snake.check_wall_collision():
#     screen.fill(colorBLACK)
#     center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#     screen.blit(game_over, center_rect)
#     pygame.display.flip()
#     pygame.time.delay(2000)
#     running = False
#     continue

#   if snake.check_collision(food):
#     if food.color == colorGREEN:
#         score += 1  # Увеличиваем очки
#     if food.color == colorBLUE:
#         score += 2
#     if food.color == colorYELLOW:
#         score += 3
#     food.randomize()
    
#   if food.is_expired():
#     food.randomize()
    
#     # Повышение уровня каждые 4 очка
#     if score % 4 == 0:
#       level += 1
#       FPS += 1  # Увеличиваем скорость игры

#   # Рисуем объекты
#   snake.draw()
#   food.draw()
#   draw_text(f"Score: {score}", 10, 10, colorBLACK)
#   draw_text(f"Level: {level}", 10, 40, colorBLACK)
  
#   pygame.display.flip()
#   clock.tick(FPS)

# pygame.quit()

# # 3)
# import pygame
# import math
# pygame.init()

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Drawing App")

# # Цвета
# colorWHITE = (255, 255, 255)
# colorBLACK = (0, 0, 0)
# colorRED = (255, 0, 0)
# colorGREEN = (0, 255, 0)
# colorBLUE = (0, 0, 255)

# # Начальные параметры
# screen.fill(colorBLACK)
# LMBpressed = False
# RMBpressed = False
# THICKNESS = 5
# mode = "brush"  # brush (кисть), rect (прямоугольник), circle (круг)
# prevX = prevY = 0
# startX = startY = 0
# rect = pygame.Rect(0, 0, 0, 0)
# circle = pygame.Rect(0, 0, 0, 0)
# rects = []  # Храним нарисованные фигуры
# circles = []
# squares = []
# r_triangles = []
# r_triangle = [] 
# e_triangles = []
# e_triangle = []
# rhombuses = []
# rhombuse = []
# drawing_surface = screen.copy()
# curr_color = colorRED  # Выбранный цвет
# clock = pygame.time.Clock()

# done = False
# while not done:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       done = True
#     elif event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_1:
#         mode = "brush"
#       elif event.key == pygame.K_2:
#         mode = "rect"
#       elif event.key == pygame.K_3:
#         mode = "circle"
#       elif event.key == pygame.K_4:
#         mode = "square"
#       elif event.key == pygame.K_5:
#         mode = "r_triangle"
#       elif event.key == pygame.K_6:
#         mode = "e_triangle"
#       elif event.key == pygame.K_7:
#         mode = "rhombus"
#       elif event.key == pygame.K_EQUALS:
#         THICKNESS += 1
#       elif event.key == pygame.K_MINUS:
#         THICKNESS = max(1, THICKNESS - 1)
#       elif event.key == pygame.K_c:
#         screen.fill(colorBLACK)
#         rects.clear()
#         circles.clear()
#         r_triangles.clear()
#         squares.clear()
#         e_triangles.clear()
#         rhombuses.clear()
#         drawing_surface = screen.copy()
#       elif event.key == pygame.K_r:
#         curr_color = colorRED
#       elif event.key == pygame.K_g:
#         curr_color = colorGREEN
#       elif event.key == pygame.K_b:
#         curr_color = colorBLUE
    
#     elif event.type == pygame.MOUSEBUTTONDOWN:
#       if event.button == 1:  # Левая кнопка (рисование)
#         LMBpressed = True
#         prevX, prevY = event.pos
#         if mode == "rect":
#           startX, startY = event.pos
#           rect = pygame.Rect(startX, startY, 0, 0)
#         elif mode == "circle":
#           startX, startY = event.pos
#           circle = pygame.Rect(startX, startY, 0, 0)
#         elif mode == "square":
#           startX, startY = event.pos
#           square = pygame.Rect(startX, startY, 0, 0)
#         elif mode == "r_triangle":
#           startX, startY = event.pos
#           r_triangle = [(startX, startY), (startX, startY), (startX, startY)]
#         elif mode == "e_triangle":
#           startX, startY = event.pos
#           e_triangle = [(startX, startY), (startX, startY), (startX, startY)]
#         elif mode == "rhombus":
#           startX, startY = event.pos
#           rhombuse = pygame.Rect(startX, startY, 0, 0)
#       elif event.button == 3:  # Правая кнопка (ластик)
#         RMBpressed = True
#         prevX, prevY = event.pos
    
#     elif event.type == pygame.MOUSEMOTION:
#       currX, currY = event.pos
#       if LMBpressed and mode == "brush":
#         pygame.draw.line(drawing_surface, curr_color, (prevX, prevY), (currX, currY), THICKNESS)
#         prevX, prevY = currX, currY
#       elif LMBpressed and mode == "rect":
#         rect.x = min(startX, currX)
#         rect.y = min(startY, currY)
#         rect.width = abs(currX - startX)
#         rect.height = abs(currY - startY)
#       elif LMBpressed and mode == "circle":
#         radius = max(abs(currX - startX), abs(currY - startY)) // 2
#         circle.x = startX - radius
#         circle.y = startY - radius
#         circle.width = circle.height = radius * 2
#       elif LMBpressed and mode == "square":
#         square.x = min(startX, currX)
#         square.y = min(startY, currY)
#         square.width = abs(currX - startX)
#         square.height = abs(currX - startX)
#       elif LMBpressed and mode == "r_triangle":
#         r_triangle = [(currX, currY), (startX, startY), (startX, currY)]  # Левый нижний угол, Левый верхний угол, Правый нижний угол
#       elif LMBpressed and mode == "e_triangle":
#         side = abs(currX - startX)  # Длина стороны
#         height = (math.sqrt(3) / 2) * side  # Высота треугольника  
#         e_triangle = [
#             (startX, startY),  # Первая вершина (начало)
#             (startX + side, startY),  # Вторая вершина (по горизонтали)
#             (startX + side / 2, startY - height)  # Третья вершина (вверх)
#         ]
#       elif LMBpressed and mode == "rhombus":
#         centerX = (startX + currX) // 2
#         centerY = (startY + currY) // 2
#         width = abs(currX - startX)
#         height = abs(currY - startY)
#         rhombus = [
#           (centerX - width // 2, centerY),  # Левая вершина
#           (centerX, centerY - height // 2), # Верхняя вершина
#           (centerX + width // 2, centerY),  # Правая вершина
#           (centerX, centerY + height // 2)  # Нижняя вершина
#         ]
#       elif RMBpressed:  # Ластик
#         pygame.draw.line(drawing_surface, colorBLACK, (prevX, prevY), (currX, currY), THICKNESS)
#         prevX, prevY = currX, currY
    
#     elif event.type == pygame.MOUSEBUTTONUP:
#       if event.button == 1:
#         LMBpressed = False
#         if mode == "rect":
#           rects.append((rect.copy(), curr_color))  # Сохраняем прямоугольник
#         elif mode == "circle":
#           circles.append((circle.copy(), curr_color))  # Сохраняем круг
#         elif mode == "square":
#           squares.append((square.copy(), curr_color))
#         elif mode == "r_triangle" and len(r_triangle) == 3:
#           r_triangles.append((r_triangle.copy(), curr_color))  # Сохраняем треугольник
#         elif mode == "e_triangle" and len(e_triangle) == 3:
#           e_triangles.append((e_triangle.copy(), curr_color))  # Сохраняем треугольник
#         elif mode == "rhombus" and len(rhombus) == 4:
#           rhombuses.append((rhombus.copy(), curr_color))
#       elif event.button == 3:
#         RMBpressed = False

#   # Перерисовываем экран
#   screen.blit(drawing_surface, (0, 0))
#   for r, color in rects:
#     pygame.draw.rect(screen, color, r, 2)
#   for c, color in circles:
#     pygame.draw.ellipse(screen, color, c, 2)
#   for s, color in squares:
#     pygame.draw.rect(screen, color, s, 2)
#   for r, color in r_triangles:
#     pygame.draw.polygon(screen, color, r, 2)
#   for e, color in e_triangles:
#     pygame.draw.polygon(screen, color, e, 2)
#   for rh, color in rhombuses:
#     pygame.draw.polygon(screen, color, rh, 2)

#   # Отображаем текущую фигуру
#   if LMBpressed and mode == "rect":
#     pygame.draw.rect(screen, curr_color, rect, 2)
#   elif LMBpressed and mode == "circle":
#     pygame.draw.ellipse(screen, curr_color, circle, 2)
#   elif LMBpressed and mode == "square":
#     pygame.draw.rect(screen, curr_color, square, 2)
#   elif LMBpressed and mode == "r_triangle" and len(r_triangle) == 3:
#     pygame.draw.polygon(screen, curr_color, r_triangle, 2)
#   elif LMBpressed and mode == "e_triangle" and len(e_triangle) == 3:
#     pygame.draw.polygon(screen, curr_color, e_triangle, 2)
#   elif LMBpressed and mode == "rhombus" and len(rhombuse) == 4:
#     pygame.draw.rect(screen, curr_color, rhombuse, 2)

#   pygame.display.flip()
#   clock.tick(60)

# pygame.quit()