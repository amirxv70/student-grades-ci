"""Учебное приложение: подсчёт успеваемости студентов."""


def average(grades):
    """Возвращает средний балл по списку оценок."""
    if not grades:
        raise ValueError("Список оценок пуст")
    return sum(grades) / len(grades)


def letter_grade(score):
    """Переводит балл (0-100) в буквенную оценку."""
    if not 0 <= score <= 100:
        raise ValueError("Балл должен быть в диапазоне 0-100")
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "F"


if __name__ == "__main__":
    marks = [95, 82, 70]
    avg = average(marks)
    print(f"Средний балл: {avg:.1f}, оценка: {letter_grade(avg)}")
