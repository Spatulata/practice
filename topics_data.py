AUTHORS = (
    "Поляков Сергей Русланович, ВО-ТМ-21",
)

TOPICS = [
    {
        "id": "types",
        "title": "1. Типы данных и изменяемость",
        "theory": (
            "У значения есть тип: int, float, str, bool, list, tuple, dict и др. "
            "Тип смотрят через type(). "
            "Неизменяемые (int, str, tuple) нельзя менять на месте. "
            "Изменяемые (list, dict, set) можно. "
            "True и False пишутся с заглавной буквы."
        ),
        "syntax": (
            "x = 10\n"
            "y = 3.14\n"
            "s = 'привет'\n"
            "flag = True\n"
            "print(type(x))"
        ),
        "example": (
            "a = [1, 2]\n"
            "b = a\n"
            "b.append(3)\n"
            "print(a)\n"
            "\n"
            "t = (1, 2)"
        ),
        "practice_hint": "Введите 42, 3.14, True, 'текст', [1, 2] или (1, 2).",
    },
    {
        "id": "list_tuple",
        "title": "2. Списки и кортежи",
        "theory": (
            "list — изменяемый, в []. tuple — неизменяемый, в (). "
            "Индексы с нуля. "
            "Список — если данные меняются. Кортеж — если фиксированные."
        ),
        "syntax": (
            "nums = [10, 20, 30]\n"
            "nums.append(40)\n"
            "point = (3, 5)\n"
            "print(nums[0], point[1])"
        ),
        "example": (
            "colors = ['red', 'green']\n"
            "colors[0] = 'blue'\n"
            "print(colors)\n"
            "\n"
            "rgb = (255, 0, 128)\n"
            "print(rgb[2])"
        ),
        "practice_hint": (
            "Нужно хранить ФИО и год поступления без случайных правок. "
            "Выберите list или tuple."
        ),
    },
    {
        "id": "dict",
        "title": "3. Словари (dict)",
        "theory": (
            "Словарь хранит пары ключ — значение. "
            "Ключ: int, str или tuple. "
            "Операции: d[key], d.get(key), keys(), values(), items()."
        ),
        "syntax": (
            "student = {'name': 'Анна', 'age': 19}\n"
            "print(student['name'])\n"
            "student['group'] = 'ИВТ-21'\n"
            "print(student.get('city', 'нет'))"
        ),
        "example": (
            "prices = {'apple': 80, 'bread': 45}\n"
            "prices['milk'] = 70\n"
            "print(prices['apple'])\n"
            "print(list(prices.keys()))"
        ),
        "practice_hint": "Введите ключ (apple) или пару ключ=цена (banana=55).",
    },
    {
        "id": "loops",
        "title": "4. Условия и циклы (break, continue, pass)",
        "theory": (
            "if / elif / else — ветки. for и while — циклы. "
            "break — выход из цикла. continue — пропуск итерации. "
            "pass — пустой блок."
        ),
        "syntax": (
            "for n in range(1, 6):\n"
            "    if n == 3:\n"
            "        continue\n"
            "    if n == 5:\n"
            "        break\n"
            "    print(n)"
        ),
        "example": (
            "for n in range(1, 6):\n"
            "    if n == 3:\n"
            "        continue\n"
            "    print(n)"
        ),
        "practice_hint": "Выберите break, continue или pass и нажмите Проверить.",
    },
    {
        "id": "comprehension",
        "title": "5. Списковые включения",
        "theory": (
            "List comprehension: [выражение for x in seq if условие]. "
            "Короче обычного цикла с append. "
            "Здесь оставляем положительные чётные числа."
        ),
        "syntax": (
            "numbers = [1, 2, 3, 4, 5, 6]\n"
            "even = [x for x in numbers if x % 2 == 0]\n"
            "print(even)"
        ),
        "example": (
            "values = [-2, -1, 0, 1, 2, 3, 4]\n"
            "result = [x for x in values if x > 0 and x % 2 == 0]\n"
            "print(result)"
        ),
        "practice_hint": "Введите числа через пробел. Останутся положительные чётные.",
    },
    {
        "id": "exceptions",
        "title": "6. Обработка исключений",
        "theory": (
            "try — код, который может упасть. except — ловит ошибку. "
            "else — если ошибки не было. finally — всегда. "
            "Частый случай: ValueError у int()."
        ),
        "syntax": (
            "try:\n"
            "    n = int(text)\n"
            "except ValueError:\n"
            "    print('нужно целое')\n"
            "else:\n"
            "    print('ok', n)\n"
            "finally:\n"
            "    print('готово')"
        ),
        "example": (
            "text = '12a'\n"
            "try:\n"
            "    print(int(text))\n"
            "except ValueError as e:\n"
            "    print('ошибка:', e)"
        ),
        "practice_hint": "Введите целое число. При ошибке программа не упадёт.",
    },
    {
        "id": "functions",
        "title": "7. Функции: *args и **kwargs",
        "theory": (
            "*args — лишние позиционные аргументы в кортеж. "
            "**kwargs — именованные аргументы в словарь. "
            "calculate_sum(*numbers) и format_report(**results) — примеры."
        ),
        "syntax": (
            "def calculate_sum(*numbers):\n"
            "    return sum(numbers)\n"
            "\n"
            "def format_report(**results):\n"
            "    for name, value in results.items():\n"
            "        print(name, value)"
        ),
        "example": (
            "print(calculate_sum(1, 2, 3))\n"
            "print(calculate_sum(10, 20))\n"
            "\n"
            "format_report(Пользователь='Анна', Балл='5/5')"
        ),
        "practice_hint": "Введите числа через пробел и нажмите «Демо *args».",
    },
]

QUIZ_MENU = {
    "id": "quiz",
    "title": "8. Итоговый тест",
}

QUIZ_QUESTIONS = [
    {
        "question": "Какой тип у [1, 2, 3]?",
        "options": ["tuple", "list", "dict", "set"],
        "answer": 1,
    },
    {
        "question": "Что из этого нельзя изменить?",
        "options": ["list", "dict", "tuple", "set"],
        "answer": 2,
    },
    {
        "question": "Какой оператор выходит из цикла сразу?",
        "options": ["continue", "pass", "break", "return"],
        "answer": 2,
    },
    {
        "question": "Для чего удобен словарь?",
        "options": [
            "хранить пары ключ — значение",
            "он всегда отсортирован",
            "его нельзя менять",
            "доступ только по номеру",
        ],
        "answer": 0,
    },
    {
        "question": "Что даст [x for x in range(5) if x % 2 == 0]?",
        "options": ["[0, 2, 4]", "[1, 3]", "[0, 1, 2, 3, 4]", "ошибку"],
        "answer": 0,
    },
    {
        "question": "Какой блок выполнится всегда в try/except?",
        "options": ["else", "finally", "except", "только try"],
        "answer": 1,
    },
    {
        "question": "Что делает *args в параметрах функции?",
        "options": [
            "собирает лишние позиционные аргументы в кортеж",
            "удаляет аргументы",
            "создаёт словарь",
            "это синтаксическая ошибка",
        ],
        "answer": 0,
    },
]
