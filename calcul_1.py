def main(input_str: str):
    """
    Основная функция, принимает строку с арифметическим выражением и возвращает результат.
    """
    # Разделяем строку на элементы
    operation = input_str.split()

    # Проверяем, что в строке ровно три элемента: два числа и один оператор
    if (len(operation) != 3 or operation[1] not in ['+', '-', '*', '/'] or
            not operation[0].isdigit() or not operation[2].isdigit()):
        raise ValueError("Формат операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")

    # Извлекаем числа и оператор
    numder_1, operator, numder_2 = operation

    # Преобразуем числа в целые
    numder_1 = int(numder_1)
    numder_2 = int(numder_2)

    # Проверяем диапазон чисел
    if not (1 <= numder_1 <= 10 and 1 <= numder_2 <= 10):
        raise ValueError("Числа должны быть в диапазоне от 1 до 10")

    # Выполняем операцию
    if operator == '+':
        result = numder_1 + numder_2
    elif operator == '-':
        result = numder_1 - numder_2
    elif operator == '*':
        result = numder_1 * numder_2
    elif operator == '/':
        if numder_2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        result = numder_1 // numder_2  # Целочисленное деление

    # Возвращаем результат в виде строки
    return str(result)