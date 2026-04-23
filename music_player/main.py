import pygame
from player import MusicPlayer

# Инициализация всех модулей Pygame
pygame.init()

# Настройки окна
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

# Инициализация шрифтов для отображения текста
font = pygame.font.SysFont(None, 48)      # Основной шрифт
small_font = pygame.font.SysFont(None, 30) # Шрифт для подсказок

# Создание экземпляра нашего плеера и таймера
player = MusicPlayer()
clock = pygame.time.Clock()

running = True
while running:
    # Ограничиваем FPS для стабильности (30 кадров в секунду)
    clock.tick(30)

    # Закрашиваем фон черным цветом перед отрисовкой каждого кадра
    screen.fill((0, 0, 0))

    # Отображение названия текущего трека
    # Используем f-строку для динамического вывода номера трека
    text = font.render(f"Now Playing: Track {player.current + 1}", True, (255, 255, 255))
    screen.blit(text, (120, 100))

    # Вывод визуальных подсказок управления на экран
    controls = [
        "P = Play | S = Stop",
        "N = Next | B = Back",
        "Space = Pause | Q = Quit"
    ]

    y_pos = 200 # Начальная позиция текста по вертикали
    for line in controls:
        help_text = small_font.render(line, True, (200, 200, 200))
        screen.blit(help_text, (180, y_pos))
        y_pos += 40 # Сдвигаем следующую строку ниже

    # ОБРАБОТКА СОБЫТИЙ
    for event in pygame.event.get():
        # Если нажата кнопка закрытия окна
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатий клавиш клавиатуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.prev()
            elif event.key == pygame.K_SPACE:
                player.pause()
            elif event.key == pygame.K_q: # Клавиша выхода
                running = False

    # Обновление дисплея
    pygame.display.flip()

# Завершение работы программы
pygame.quit()