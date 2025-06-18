from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd
from matplotlib import pyplot as plt
import os
import numpy as np

# Инициализация драйвера
driver = webdriver.Chrome()

# URL страницы "Все диваны"
# url = 'https://www.divan.ru/sankt-peterburg/category/pramye-divany'

# Локально сохранённая mhtml-страница
current_dir = os.path.dirname(os.path.abspath(__file__))
url = os.path.join(current_dir, 'Divan.ru.mhtml')

# Открываем выбранный вариант
driver.get(url)
time.sleep(5)

# Парсинг цен с добавлением в список
prices = []
for element in driver.find_elements(By.CSS_SELECTOR, ".ui-LD-ZU.KIkOH"):
    try:
        # Очистка текста и преобразование в число
        text = element.text.replace('руб.', '').replace(' ', '').strip()
        if text:  # Проверка на пустую строку
            price = int(text)
            prices.append(price)
    except Exception as e:
        print(f"Ошибка парсинга цены: {element.text} | Ошибка: {e}")

# Проверка на наличие данных
if not prices:
    print("Не найдено ни одной цены!")
    driver.quit()
    exit()

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price])

# Закрытие драйвера
driver.quit()

# Чтение из файла
df = pd.read_csv('prices.csv')

# Обработка пропущенных значений
print(f"Найдено пропущенных значений: {df['Price'].isna().sum()}")
df = df.dropna(subset=['Price'])  # Удаление строк с пропущенными ценами

# Преобразование нечисловых значений
try:
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
except Exception as e:
    print(f"Ошибка преобразования цен: {e}")
    df['Price'] = pd.to_numeric(df['Price'].astype(str).str.replace(r'\D', '', regex=True), errors='coerce')

# Удаление некорректных значений после преобразования
df = df.dropna(subset=['Price'])
df = df[df['Price'] > 0]  # Удаление нулевых и отрицательных цен

# Проверка, остались ли данные
if df.empty:
    print("Нет данных для анализа!")
    exit()

# Рассчитываем статистику
mean_price = int(df['Price'].mean())
median_price = int(df['Price'].median())
min_price = int(df['Price'].min())
max_price = int(df['Price'].max())

# Выводим статистику
print(f"Статистика цен на диваны:")
print(f" - Средняя цена: {mean_price} руб.")
print(f" - Медианная цена: {median_price} руб.")
print(f" - Минимальная цена: {min_price} руб.")
print(f" - Максимальная цена: {max_price} руб.")

# Создаем гистограмму с улучшенной визуализацией
plt.figure(figsize=(12, 8))

# Гистограмма с автоматическим расчетом бинов
n, bins, patches = plt.hist(df['Price'],
                            bins='auto',  # Автоматический расчет интервалов
                            color='skyblue',
                            edgecolor='black',
                            alpha=0.8)

# Добавляем линии статистик
plt.axvline(mean_price, color='red', linestyle='dashed', linewidth=2, label=f'Средняя: {mean_price} руб.')
plt.axvline(median_price, color='green', linestyle='dashed', linewidth=2, label=f'Медиана: {median_price} руб.')

# Настройка оформления
plt.title('Распределение цен на диваны', fontsize=16)
plt.xlabel('Цена, руб.', fontsize=14)
plt.ylabel('Количество предложений', fontsize=14)
plt.grid(axis='y', alpha=0.3)
plt.legend()
plt.tight_layout()

# Сохраняем гистограмму в файл
plt.savefig('prices_histogram.png',
           dpi=300,
           bbox_inches='tight',
           facecolor='white')

print("Гистограмма сохранена в файл 'prices_histogram.png'")

# Дополнительно: создаем boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(df['Price'], vert=False, patch_artist=True)
plt.title('Boxplot цен на диваны', fontsize=16)
plt.xlabel('Цена, руб.', fontsize=14)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('prices_boxplot.png', dpi=300)
print("Boxplot сохранен в файл 'prices_boxplot.png'")

# Показываем графики
plt.show()