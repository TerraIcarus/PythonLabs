var employees = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "department": "Бухгалтерия",
        "expenses": [450, 1200, 300]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "department": "Отдел продаж",
        "expenses": [800, 250, 600]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "department": "IT-отдел",
        "expenses": [1500, 700, 350]
    },
    {
        "name": "Андрей",
        "surname": "Соколов",
        "department": "Бухгалтерия",
        "expenses": [500, 700, 900]
    },
    {
        "name": "Дмитрий",
        "surname": "Козлов",
        "department": "Отдел продаж",
        "expenses": [300, 400, 500]
    }
];

var rpad = function(str, length) {

    str = str.toString();

    while (str.length < length)
        str = str + ' ';

    return str;
};


var printEmployees = function(employees) {

    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Отдел", 20),
        rpad("Расходы", 20)
    );

    for (var i = 0; i <= employees.length - 1; i++) {

        console.log(
            rpad(employees[i]['name'], 15),
            rpad(employees[i]['surname'], 15),
            rpad(employees[i]['department'], 20),
            rpad(employees[i]['expenses'], 20)
        );
    }

    console.log('\n');
};

printEmployees(employees);

// Функция фильтрации сотрудников по отделу

var filterEmployees = function(employees, department) {

    var result = [];

    for (var i = 0; i <= employees.length - 1; i++) {

        if (employees[i]['department'] == department) {
            result.push(employees[i]);
        }
    }

    return result;
};


// Ввод названия отдела пользователем

var department = prompt("Введите название отдела:");


// Получение отфильтрованного списка сотрудников

var filteredEmployees = filterEmployees(employees, department);


// Вывод результата

console.log("Сотрудники выбранного отдела:");
printEmployees(filteredEmployees);


// Функция фильтрации по средней сумме расходов

var filterEmployees = function(employees, minAverage) {

    var result = [];

    for (var i = 0; i <= employees.length - 1; i++) {

        var sum = 0;

        for (var j = 0; j <= employees[i]['expenses'].length - 1; j++) {
            sum = sum + employees[i]['expenses'][j];
        }

        var average = sum / employees[i]['expenses'].length;

        if (average > minAverage) {
            result.push(employees[i]);
        }
    }

    return result;
};


// Ввод минимальной средней суммы расходов

var minAverage = parseFloat(prompt("Введите среднюю сумму расходов:"));


// Получение отфильтрованного списка сотрудников

var filteredEmployees = filterEmployees(employees, minAverage);


// Вывод результата

console.log("Сотрудники со средней суммой расходов выше заданного значения:");
printEmployees(filteredEmployees);
