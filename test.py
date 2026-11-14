class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Ошибка: Корень из отрицательного числа не определен ")
    return x ** 0.5

try:
    num = int(input())
    result = square_root(num)
    print(result)

except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Ошибка: введено не число")