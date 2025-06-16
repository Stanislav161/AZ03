import matplotlib.pyplot as plt
import numpy as np

# Параметры нормального распределения
mean = 0        # Среднее значение
std_dev = 1     # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределённых по нормальному закону
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins=30, density=True, edgecolor='black')

# Настройка графика
plt.title('Гистограмма нормально распределённых данных')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.legend()

# Показ графика
plt.show()