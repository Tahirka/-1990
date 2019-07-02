import sys
import pygame
import random

pygame.init()

width = 520
height = 540
# Размер танка
tank_length = 36
tank_width = 36
# Начальное положение танка
x_coord = [175]
y_coord = [520]
# Начальная скорость танка
x_speed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y_speed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Последнее направление движения танка
last_move = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Начальная скорость пули
x_bullet_speed = 0
y_bullet_speed = 0
# Начальное положение пули
x_bullet_coord = 1000
y_bullet_coord = 1000
# Создаём объекты(первые 8 неразрушимые затем база)
x_object_coord = [0, 20, 480, 500, 240, 260, 240, 260, 240, 260, 240, 260, 220, 220, 240, 260, 280, 280]
y_object_coord = [260, 260, 260, 260, 120, 120, 140, 140, 500, 500, 520, 520, 500, 520, 480, 480, 500, 520]
for w in range(2):
    for q in range(6):
        for i in range(9-w):
            x_object_coord.append(40 + q * 80)
            x_object_coord.append(60 + q * 80)
            y_object_coord.append(20 * i + 40 + w * 300)
            y_object_coord.append(20 * i + 40 + w * 300)

object_size = 20
# Целостность базы
z = 1
# Массив для конца игры
g = []
h = []
# Куча одинаковых переменных чтобы не писать по сто раз
a = 1 #Скорость танка
b = 2.5 #Скорость пули
f = 0
l = 0
m = 0
n = 0
o = 0
p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Переменные для волшебства
x_bullet_speed_ = 0
y_bullet_speed_ = 0
x_bullet_coord_ = 0
y_bullet_coord_ = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Сражайся или умри')
clock = pygame.time.Clock()

while True:
    #dt = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        # Когда нажаты стрелки изменяем скорость танка
        # чтобы он ехал

        if event.type == pygame.KEYDOWN:
            y_speed[0] == 0
            x_speed[0] == 0
            if event.key == pygame.K_a :
                x_speed[0] = -a
                last_move[0] = 1
            elif event.key == pygame.K_d :
                x_speed[0] = a
                last_move[0] = 2
            elif event.key == pygame.K_w :
                y_speed[0] = -a
                last_move[0] = 3
            elif event.key == pygame.K_s:
                y_speed[0] = a
                last_move[0] = 4

        # Когда стрелки не нажаты скорость ставим в ноль
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: x_speed[0] = 0
            if event.key == pygame.K_d: x_speed[0] = 0
            if event.key == pygame.K_w: y_speed[0] = 0
            if event.key == pygame.K_s: y_speed[0] = 0

    # Появление танков
    for i in range(20):
        if l == i * 250:
            k = i % 3
            x_coord.append(k * 240)
            y_coord.append(0)
            o +=1
    # Движение танков
    if len(x_coord) > 1:
        if l == n * 30:
            for j in range(1, len(x_coord)):
                x_speed[j] = 0
                y_speed[j] = 0
                last_move[j] = random.randrange(1, 5)
                if last_move[j] == 1:
                    x_speed[j] = -a
                if last_move[j] == 2:
                    x_speed[j] = a
                if last_move[j] == 1:
                    y_speed[j] = -a
                if last_move[j] == 1:
                    y_speed[j] = a
                    p[j] = l
            n += 1
        for j in range(1, len(x_coord)):
            if p[j] + 100 > l:
                x_speed[j] = 0
                y_speed[j] = 1
    l += 1

    # Меняем положение танка не выходя за рамки окна и не заходя за обьекты
    for j in range(len(x_coord)):
        if x_coord[j] < 0: x_coord[j] = 0
        if x_coord[j] > 485: x_coord[j] = 485
        if y_coord[j] < 0: y_coord[j] = 0
        if y_coord[j] > 505: y_coord[j] = 505
        for i in range(len(x_object_coord)):
            if x_coord[j] + 36 == x_object_coord[i] and y_coord[j] + 36 >= y_object_coord[i] >= y_coord[j] - 20:x_coord[j] -= a
            if x_coord[j] - 20 == x_object_coord[i] and y_coord[j] + 36 >= y_object_coord[i] >= y_coord[j] - 20:x_coord[j] += a
            if y_coord[j] + 36 == y_object_coord[i] and x_coord[j] + 36 >= x_object_coord[i] >= x_coord[j] - 20:y_coord[j] -= a
            if y_coord[j] - 20 == y_object_coord[i] and x_coord[j] + 36 >= x_object_coord[i] >= x_coord[j] - 20:y_coord[j] += a

        x_coord[j] = x_coord[j] + x_speed[j]
        y_coord[j] = y_coord[j] + y_speed[j]


    # Взаимодействия танков
    for j in range(len(x_coord)):
        for i in range(len(x_coord)):
            if x_coord[j] + 36 == x_coord[i] and y_coord[j] + 36 >= y_coord[i] >= y_coord[j] - 36:x_coord[j], x_coord[i] = x_coord[j] - a, x_coord[i] + a
            if x_coord[j] - 36 == x_coord[i] and y_coord[j] + 36 >= y_coord[i] >= y_coord[j] - 36:x_coord[j], x_coord[i] = x_coord[j] + a, x_coord[i] - a
            if y_coord[j] + 36 == y_coord[i] and x_coord[j] + 36 >= x_coord[i] >= x_coord[j] - 36:y_coord[j], y_coord[i] = y_coord[j] - a, x_coord[i] + a
            if y_coord[j] - 36 == y_coord[i] and x_coord[j] + 36 >= x_coord[i] >= x_coord[j] - 36:y_coord[j], y_coord[i] = y_coord[j] + a, x_coord[i] - a

    for q in range(1, len(x_coord)):  # Разрушение танков
        if x_coord[q] - 4 <= x_bullet_coord <= x_coord[q] + 44 and y_coord[q] - 4 <= y_bullet_coord <= y_coord[q] + 44:
            x_bullet_speed_, y_bullet_speed_ = 0, b * 3
            x_bullet_coord_, y_bullet_coord_ = 540, 540
            m = q
    if m != 0:
        x_coord.pop(m)
        y_coord.pop(m)
        m = 0

            # Пуля
    if pygame.key.get_pressed()[pygame.K_SPACE] and (x_bullet_coord > 680 or x_bullet_coord < 0 or y_bullet_coord > 680
                                                 or y_bullet_coord < 0):
        if last_move[0] == 1:
            x_bullet_speed = -b
        if last_move[0] == 2:
            x_bullet_speed = b
        if last_move[0] == 3:
            y_bullet_speed = -b
        if last_move[0] == 4:
            y_bullet_speed = b
        if x_bullet_speed != 0:
            y_bullet_speed = 0
        x_bullet_coord = x_coord[0] + tank_length/2
        y_bullet_coord = y_coord[0] + tank_width/2
    if(x_bullet_coord > 700) or(x_bullet_coord < 0) or(y_bullet_coord > 700) or(y_bullet_coord < 0) :
        x_bullet_coord = 1000
        y_bullet_coord = 1000
        x_bullet_speed = 0
        y_bullet_speed = 0

    # Неразрушимые
    for i in range(8):
        if x_object_coord[i] - 4 <= x_bullet_coord <= x_object_coord[i] + 24 and y_object_coord[i] - 4 \
                    <= y_bullet_coord <= y_object_coord[i] + 24:
            x_bullet_speed_, y_bullet_speed_ = 0, b*3 # фиксит несколько вылетов пули от одного нажатия
            x_bullet_coord_, y_bullet_coord_ = 540, 540 # фиксит несколько вылето пули от одного нажатия
    # База
    for i in range(8, 12):
        if x_object_coord[i] - 4 <= x_bullet_coord <= x_object_coord[i] + 24 and y_object_coord[i] - 4 \
                    <= y_bullet_coord <= y_object_coord[i] + 24:
            x_bullet_speed_, y_bullet_speed_ = 0, b*3 # фиксит несколько вылето пули от одного нажатия
            x_bullet_coord_, y_bullet_coord_ = 540, 540 # фиксит несколько вылетов пули от одного нажатия
            z = 0
    # Разрушимые

    for i in range(12, len(x_object_coord) - 3):
        for q in range(3):# Разрушение нескольких обьектов одновременно
            if x_object_coord[i+q] - 4 <= x_bullet_coord <= x_object_coord[i+q] + 24 and y_object_coord[i+q] - 4 \
                    <= y_bullet_coord <= y_object_coord[i+q] + 24:
                x_bullet_speed_, y_bullet_speed_ = 0, b*3 # фиксит несколько вылетов пули от одного нажатия
                x_bullet_coord_, y_bullet_coord_ = 540, 540 # фиксит несколько вылетов пули от одного нажатия
                x_object_coord[i+q], y_object_coord[i+q] = 1200, 1200
    if y_bullet_coord_ == 540:
        x_bullet_speed, y_bullet_speed = x_bullet_speed_, y_bullet_speed_
        x_bullet_coord, y_bullet_coord = x_bullet_coord, y_bullet_coord_
    y_bullet_coord_ = 541
    x_bullet_coord += x_bullet_speed
    y_bullet_coord += y_bullet_speed



    # Немного повторяющихся переменных
    c = 8
    d = 20
    e = 12
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (192, 192, 192), (int(x_bullet_coord), int(y_bullet_coord)), 4)
    for j in range(1,len(x_coord)):
        pygame.draw.rect(screen, (119, 136, 153), (int(x_coord[j]), int(y_coord[j]), tank_width, tank_length))
    pygame.draw.rect(screen, (255, 215, 0), (int(x_coord[0]), int(y_coord[0]), tank_width, tank_length))
    # Прорисовка частей танка
    if last_move[0] == 1:
        pygame.draw.rect(screen, (0, 0, 0), (int(x_coord[0]), int(y_coord[0])+c, tank_width, d))
        pygame.draw.circle(screen, (255, 215, 0), (int(x_coord[0]) + 20, int(y_coord[0] + 18)), 12)
        pygame.draw.rect(screen, (255, 215, 0), (int(x_coord[0])-5, int(y_coord[0])+16, 15, 4))
    if last_move[0] == 2:
        pygame.draw.rect(screen, (0, 0, 0), (int(x_coord[0]), int(y_coord[0])+c, tank_width, d))
        pygame.draw.circle(screen, (255, 215, 0), (int(x_coord[0]) + 16, int(y_coord[0] + 18)), 12)
        pygame.draw.rect(screen, (255, 215, 0), (int(x_coord[0])+26, int(y_coord[0])+16, 15, 4))
    if last_move[0] == 3:
        pygame.draw.rect(screen, (0, 0, 0), (int(x_coord[0])+c, int(y_coord[0]), d, tank_length))
        pygame.draw.circle(screen, (255, 215, 0), (int(x_coord[0] + 18) , int(y_coord[0]) + 20), 12)
        pygame.draw.rect(screen, (255, 215, 0), (int(x_coord[0])+16, int(y_coord[0])-5, 4, 15))
    if last_move[0] == 4:
        pygame.draw.rect(screen, (0, 0, 0), (int(x_coord[0])+c, int(y_coord[0]), d, tank_length))
        pygame.draw.circle(screen, (255, 215, 0), (int(x_coord[0] + 18) , int(y_coord[0]) + 16), 12)
        pygame.draw.rect(screen, (255, 215, 0), (int(x_coord[0])+16, int(y_coord[0])+26, 4, 15))
    for i in range(8):
        pygame.draw.rect(screen, (250, 250, 250), (x_object_coord[i], y_object_coord[i], object_size, object_size))
        pygame.draw.rect(screen, (192, 192, 192), (x_object_coord[i] + 18, y_object_coord[i], 2, 20))
        pygame.draw.rect(screen, (192, 192, 192), (x_object_coord[i], y_object_coord[i] + 18, 20, 2))
        pygame.draw.rect(screen, (192, 192, 192), (x_object_coord[i], y_object_coord[i], 2, 20))
        pygame.draw.rect(screen, (192, 192, 192), (x_object_coord[i], y_object_coord[i], 20, 2))
    for i in range(12,len(x_object_coord)):
        pygame.draw.rect(screen, (128, 0, 0), (x_object_coord[i], y_object_coord[i], object_size, object_size))
        pygame.draw.rect(screen, (128, 128, 128), (x_object_coord[i] + 18, y_object_coord[i], 2, 20))
        pygame.draw.rect(screen, (128, 128, 128), (x_object_coord[i], y_object_coord[i] + 18, 20, 2))
        pygame.draw.rect(screen, (128, 128, 128), (x_object_coord[i], y_object_coord[i], 2, 20))
        pygame.draw.rect(screen, (128, 128, 128), (x_object_coord[i], y_object_coord[i], 20, 2))
    if z == 1:
        for i in range(8, 12):
            pygame.draw.rect(screen, (0, 220, 0), (x_object_coord[i], y_object_coord[i], object_size, object_size))
    if z == 0:
        for i in range(8, 12):
            pygame.draw.rect(screen, (178, 34, 34), (x_object_coord[i], y_object_coord[i], object_size, object_size))
        f += 1
        if f >= 50:
            screen.fill((255, 255, 255))
            myfont = pygame.font.SysFont('Comic Sans MS', 120)
            textsurface = myfont.render('Ты плох!', False, (0, 0, 0))
            screen.blit(textsurface, (0, 100))
    if o == 20 and len(x_coord) == 1:
        f += 1
        if f >= 25:
            screen.fill((255, 255, 255))
            myfont = pygame.font.SysFont('Comic Sans MS', 120)
            textsurface = myfont.render('А ты ', False, (0, 0, 0))
            screen.blit(textsurface, (100, 20))
            myfont = pygame.font.SysFont('Comic Sans MS', 120)
            textsurface = myfont.render('неплох!', False, (0, 0, 0))
            screen.blit(textsurface, (50, 200))

    pygame.display.flip()