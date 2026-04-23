
import pygame

# Инициализация всех модулей Pygame
pygame.init()

# Устанавливаем ширину и высоту окна
W = 800
H = 480
# Радиус шарика
R = 25

# Создаем окно приложения
screen = pygame.display.set_mode((W, H))
# Устанавливаем заголовок окна
pygame.display.set_caption("Moving Ball")

# Начальные координаты шарика (центр экрана)
circle_x = W // 2
circle_y = H // 2

# Создаем объект для управления частотой кадров (FPS)
clock = pygame.time.Clock()

# Флаг для работы игрового цикла
running = True

# ГЛАВНЫЙ ЦИКЛ ПРОГРАММЫ
while running:
    # Очищаем экран белым цветом перед отрисовкой нового кадра
    # Это предотвращает появление "шлейфа" от шарика
    screen.fill('white')

    # Обработка событий
    for event in pygame.event.get():
        # Если нажали на крестик — завершаем программу
        if event.type == pygame.QUIT:
            running = False

        # Проверяем нажатие клавиш
        if event.type == pygame.KEYDOWN:
            # Движение ВВЕРХ: проверяем, что верхний край шарика не выйдет за 0
            if event.key == pygame.K_UP and circle_y - 20 - R >= 0:
                circle_y -= 20
            # Движение ВНИЗ: проверяем, что нижний край не выйдет за высоту окна
            elif event.key == pygame.K_DOWN and circle_y + 20 + R <= H:
                circle_y += 20
            # Движение ВЛЕВО: проверяем, что левый край не уйдет за 0
            elif event.key == pygame.K_LEFT and circle_x - 20 - R >= 0:
                circle_x -= 20
            # Движение ВПРАВО: проверяем, что правый край не выйдет за ширину окна
            elif event.key == pygame.K_RIGHT and circle_x + 20 + R <= W:
                circle_x += 20

    # Отрисовка шарика: (экран, цвет, (координаты X, Y), радиус)
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), R)

    # Обновляем экран, чтобы отобразить изменения
    pygame.display.flip()
    
    # Ограничиваем количество кадров (например, 60 FPS для стабильной работы)
    clock.tick(60)

# Выход из Pygame при завершении цикла
pygame.quit()