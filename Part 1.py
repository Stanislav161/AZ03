import matplotlib.pyplot as plt
import numpy as np


# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных данных
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))  # Размер графика
plt.hist(data,
         bins=30,            # Количество столбцов
         density=True,       # Нормализация площади под кривой
         alpha=0.7,          # Прозрачность столбцов
         color='skyblue',     # Цвет столбцов
         edgecolor='black')  # Цвет границ столбцов
         label='Сгенерированные данные')  # Добавлена метка

# Добавление идеальной кривой нормального распределения
x = np.linspace(-4, 4, 1000)
pdf = (1/(std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
plt.plot(x, pdf, 'r-', linewidth=2, label='Теоретическая плотность')

# Настройка оформления
plt.title('Гистограмма нормального распределения', fontsize=14)
plt.xlabel('Значения', fontsize=12)
plt.ylabel('Плотность вероятности', fontsize=12)
plt.grid(alpha=0.3)          # Полупрозрачная сетка
plt.legend()                 # Отображение легенды

# Сохранение в файл (добавлено)
plt.savefig('normal_distribution.png',  # Имя файла
            dpi=300,                   # Высокое разрешение
            bbox_inches='tight',       # Обрезать пустые поля
            facecolor='white')         # Фон

# Отображение графика
plt.show()