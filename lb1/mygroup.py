
groupmates = [
    {
        "name": "Кирилл",
        "surname": "Дружинин",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Татьяна",
        "surname": "Мазунина",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [5, 5, 5]
    },
    {
            "name": "Михаил",
            "surname": "Караичев",
            "exams": ["История", "АиГ", "КТП"],
            "marks": [4, 4, 4]
        },
        
    {
        "name": "Владислав",
        "surname": "Качаев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Семен",
        "surname": "Кирокосьянц",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Колтышева",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 5, 3]
    }
]

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Средний балл")
    for student in students:
        average = sum(student["marks"]) / len(student["marks"])
        print(student["name"].ljust(15), student["surname"].ljust(15), round(average, 2))

def filter_students(students, min_average):
    result = []
    for student in students:
        average = sum(student["marks"]) / len(student["marks"])
        if average > min_average:
            result.append(student)
    return result

min_average = float(input("Введите минимальный средний балл: "))

filtered_students = filter_students(groupmates, min_average)

print_students(filtered_students)