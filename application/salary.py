import random


def calculate_salary():
    print('Расчет зарплаты')
    return [random.randint(50000, 65000) for i in range(11)]