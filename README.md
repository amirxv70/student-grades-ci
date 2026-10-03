# Student Grades — учебный проект CI/CD

Небольшое Python-приложение для подсчёта успеваемости студентов
(средний балл и перевод балла в буквенную оценку).
Проект создан для демонстрации CI/CD-конвейера на GitHub Actions.

## Структура

```
src/grades.py             # исходный код
tests/test_grades.py      # unit-тесты (pytest)
requirements.txt          # зависимости
.github/workflows/ci.yml  # конфигурация CI/CD
```

## Запуск

```bash
pip install -r requirements.txt
python -m src.grades
```

## Тесты

```bash
pytest -v
```

## CI/CD

При каждом `push` и `pull request` GitHub Actions выполняет два этапа:
**Build** (установка зависимостей и проверка сборки) → **Test** (запуск pytest).

���������: ��������� �������� pipeline.
