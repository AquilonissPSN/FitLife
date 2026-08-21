WATER_PER_KG = 30
WATER_PER_LITTER = 1000
SEPARATOR_LENGTH = 50

user_name = input('Введите Ваше имя: ')

try:
    user_age = int(input(f'{user_name}, укажите Ваш возраст: '))
    user_weight = float(input(f'{user_name}, укажите Ваш вес (в кг.): '))
    user_height = float(input(f'{user_name}, укажите Ваш рост (в метрах): '))
except ValueError:
    print('Ошибка: возраст, вес и рост должны быть указаны числами!')
    exit(1)

bmi = round(user_weight / (user_height ** 2), 1)

water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / WATER_PER_LITTER, 1)

print(f'Здравствуйте, {user_name}! Ваш ИМТ: {bmi}')
print(
    f'Вам нужно пить {water_l} л. воды в день',
    '-' * SEPARATOR_LENGTH,
    sep='\n'
)
print('Расчет окончен. Будьте здоровы!')
