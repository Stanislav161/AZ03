import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
np.random.seed(42)  # Для воспроизводимости результатов
num_points = 100    # Количество точек

# Создание массивов случайных чисел
x = np.random.rand(num_points)  # Координаты X
y = np.random.rand(num_points)  # Координаты Y

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 6))  # Размер графика
plt.scatter(x, y,
            alpha=0.7,        # Прозрачность точек
            c='green',        # Цвет точек
            edgecolors='black', # Границы точек
            s=50)             # Размер точек

# Настройка оформления
plt.title('Диаграмма рассеяния случайных данных', fontsize=14)
plt.xlabel('X значения', fontsize=12)
plt.ylabel('Y значения', fontsize=12)
plt.grid(alpha=0.3)  # Полупрозрачная сетка

# Сохранение в файл
plt.savefig('scatter_plot.png',
            dpi=300,
            bbox_inches='tight',
            facecolor='white')

# Отображение графика
plt.show()