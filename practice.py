import ast
import os
from datetime import datetime


def detect_value_type(raw):
    text = raw.strip()
    if text == "":
        raise ValueError("Пустой ввод")
    if text in ("true", "false"):
        raise ValueError("Нужно True или False")
    try:
        value = ast.literal_eval(text)
    except (ValueError, SyntaxError):
        return "str", text
    return type(value).__name__, value


def choose_structure(choice):
    c = choice.strip().lower()
    if c == "tuple":
        return True, "Верно, здесь лучше tuple"
    if c == "list":
        return False, "Неверно: list можно менять, нужен tuple"
    return False, "Выберите list или tuple"


def demo_loop_control(mode):
    result = []
    for n in range(1, 9):
        if mode == "continue":
            if n % 2 == 0:
                continue
            result.append(n)
        elif mode == "break":
            if n == 5:
                break
            result.append(n)
        elif mode == "pass":
            if n == 3:
                pass
            result.append(n)
        else:
            raise ValueError("Выберите break, continue или pass")

    if mode == "continue":
        note = "чётные пропущены"
    elif mode == "break":
        note = "стоп на 5"
    else:
        note = "pass ничего не делает, все числа на месте"
    return "Режим {}: {}\n{}".format(mode, result, note)


def lookup_or_update_dict(catalog, raw):
    text = raw.strip()
    if text == "":
        raise ValueError("Введите ключ или ключ=цена")

    if "=" in text:
        key, price_text = text.split("=", 1)
        key = key.strip()
        price_text = price_text.strip()
        if key == "":
            raise ValueError("Ключ пустой")
        try:
            price = int(price_text)
        except ValueError:
            raise ValueError("Цена должна быть целым числом")
        catalog[key] = price
        return catalog, "Добавлено: {} = {}. Словарь: {}".format(key, price, catalog)

    if text in catalog:
        return catalog, "Цена {}: {}".format(text, catalog[text])
    return catalog, "Ключ {} не найден. Есть: {}".format(text, list(catalog.keys()))


def filter_positive_even(raw):
    text = raw.strip()
    if text == "":
        raise ValueError("Введите числа через пробел")

    values = []
    for token in text.split():
        try:
            values.append(int(token))
        except ValueError:
            raise ValueError(token + " — не целое число")

    return [x for x in values if x > 0 and x % 2 == 0]


def safe_parse_int(raw):
    text = raw.strip()
    try:
        number = int(text)
    except ValueError:
        return False, "Ошибка: нужно целое число"
    else:
        return True, "Ок: число = {}, квадрат = {}".format(number, number ** 2)
    finally:
        pass


def calculate_sum(*numbers):
    return sum(numbers)


def format_report(**results):
    lines = ["Отчёт: Основы Python", "=" * 40]
    for name, value in results.items():
        lines.append(str(name) + ": " + str(value))
    lines.append("Дата: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return "\n".join(lines)


def default_report_path(filename="result_report.txt"):
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, filename)


def save_report(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def score_quiz(answers, correct):
    total = len(correct)
    answered = sum(1 for a in answers[:total] if a is not None)
    right = sum(
        1
        for i, expected in enumerate(correct)
        if i < len(answers) and answers[i] == expected
    )
    percent = 0.0 if total == 0 else right / total * 100
    return right, total, percent, answered
