import matplotlib.pyplot as plt
import numpy as np

# Параметры нормального распределения
mean = 0
std_dev = 1
num_samples = 1000

# Генерация данных
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы с меткой
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(data,
                            bins=30,
                            density=True,
                            alpha=0.7,
                            color='skyblue',
                            edgecolor='black',
                            label='Сгенерированные данные')  # Добавлена метка

# Теоретическая кривая с меткой
x = np.linspace(-4, 4, 1000)
pdf = (1/(std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
plt.plot(x, pdf, 'r-', linewidth=2, label='Теоретическая плотность')

# Настройки оформления
plt.title('Гистограмма нормального распределения', fontsize=14)
plt.xlabel('Значения', fontsize=12)
plt.ylabel('Плотность вероятности', fontsize=12)
plt.grid(alpha=0.3)
plt.legend()  # Теперь здесь будут две записи

# Сохраняем диаграмму перед отображением
plt.savefig('normal_distribution.png',
            dpi=300,
            bbox_inches='tight',
            facecolor='white')

# Отображаем график
plt.show()