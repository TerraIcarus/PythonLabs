
groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "department": "Бухгалтерия",
        "expenses": ["Канцелярские товары", "Хозяйственные товары"],
        "amounts": [1500, 800]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "department": "Отдел продаж",
        "expenses": ["Офисная техника", "Канцелярские товары"],
        "amounts": [5000, 1200]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "department": "IT-отдел",
        "expenses": ["Компьютерные комплектующие", "Канцелярские товары"],
        "amounts": [4500, 900]
    },
    {
        "name": "Мария",
        "surname": "Соколова",
        "department": "Бухгалтерия",
        "expenses": ["Канцелярские товары", "Хозяйственные товары"],
        "amounts": [700, 1100]
    },
    {
        "name": "Анна",
        "surname": "Кузнецова",
        "department": "Отдел кадров",
        "expenses": ["Канцелярские товары", "Офисная техника"],
        "amounts": [600, 3500]
    },
    {
        "name": "Дмитрий",
        "surname": "Волков",
        "department": "IT-отдел",
        "expenses": ["Компьютерные комплектующие", "Офисная техника"],
        "amounts": [3000, 6000]
    }
]

def print_employees(employees):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Отдел".ljust(20), "Общая сумма расходов")
    for employee in employees:
        total = sum(employee["amounts"])
        print(employee["name"].ljust(15), employee["surname"].ljust(15), employee["department"].ljust(20), total)

def filter_employees(employees, min_amount):
    result = []
    for employee in employees:
        total = sum(employee["amounts"])
        if total > min_amount:
            result.append(employee)
    return result

min_amount = float(input("Введите минимальную сумму расходов: "))

filtered_employees = filter_employees(groupmates, min_amount)

print_employees(filtered_employees)