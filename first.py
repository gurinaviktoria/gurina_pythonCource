def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка! Ділення на нуль."


def main():
    print("Простий калькулятор")
    print("Операції: +, -, *, /")

    a = float(input("Введіть перше число: "))
    operation = input("Введіть операцію (+, -, *, /): ")
    b = float(input("Введіть друге число: "))

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        result = "Невірна операція!"

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
