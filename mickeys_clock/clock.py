import pygame
from clock import time_angle

# Инициализируем все модули библиотеки Pygame для работы графики и событий
pygame.init()

# Устанавливаем размеры окна (ширина и высота)
WIDTH, HEIGHT = 800, 600
# Вычисляем центр экрана, чтобы стрелки часов крутились ровно посередине
center = (WIDTH // 2, HEIGHT // 2)

# Создаем графическое окно приложения
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загружаем изображения из папки images
# .convert_alpha() рекомендуется для картинок с прозрачностью (PNG)
main = pygame.image.load("images/clock.png")
left = pygame.image.load("images/sec_hand.png")
right = pygame.image.load("images/min_hand.png")

# Создаем экземпляр класса для вычисления углов поворота стрелок
x = time_angle()
# Создаем объект Clock для ограничения частоты кадров (чтобы не перегружать процессор)
clock = pygame.time.Clock()

# Флаг состояния игры: если True, цикл продолжается
running = True

# Главный цикл игры (Game Loop)
while running:
    # 1. ОБРАБОТКА СОБЫТИЙ: проверяем действия пользователя
    for event in pygame.event.get():
        # Если пользователь нажал кнопку закрытия окна (крестик)
        if event.type == pygame.QUIT:
            running = False # Выходим из цикла

    # 2. ОБНОВЛЕНИЕ ЛОГИКИ: пересчитываем время и углы для стрелок
    x.update()

    # 3. ОТРИСОВКА КАДРА:
    # Рисуем фон (циферблат) в левом верхнем углу (0,0)
    screen.blit(main, (0, 0))
    # Рисуем кружок в центре, имитирующий крепление стрелок
    pygame.draw.circle(screen, (200, 100, 200), center, 10)

    # Поворачиваем стрелки на основе вычисленных углов из класса time_angle
    # Отрицательный знак '-' нужен для корректного направления вращения в Pygame
    rotated_left_hand = pygame.transform.rotate(left, -x.s_angle)
    rotated_rigth_hand = pygame.transform.rotate(right, -x.m_angle)

    # Получаем прямоугольники (Rect) объектов для их центрирования
    # Это важно: без этого стрелки при повороте будут «прыгать» по экрану
    rect_l = rotated_left_hand.get_rect(center=center)
    rect_r = rotated_rigth_hand.get_rect(center=center)

    # Отображаем повернутые стрелки на экране с учетом рассчитанных координат
    screen.blit(rotated_left_hand, rect_l)
    screen.blit(rotated_rigth_hand, rect_r)

    # Обновляем содержимое дисплея (показываем всё, что нарисовали за этот кадр)
    pygame.display.flip()

    # Ограничиваем цикл до 60 итераций в секунду (60 FPS)
    clock.tick(60)

# Корректное завершение работы программы
pygame.quit()