import math

def solve(a, b, c):
    # Проверяем, что все коэффициенты являются конечными числами
    if not all(map(math.isfinite, [a, b, c])):
        raise ValueError("Коэффициенты должны быть конечными.")

    # Проверка на то, что a не равно 0
    if abs(a) < 1e-9:
        raise ValueError("Коэффициент а не может быть нулём.")

    # Вычисляем дискриминант
    discriminant = b ** 2 - 4 * a * c

    # Сравниваем дискриминант с нулем с учетом эпсилон
    epsilon = 1e-9
    if discriminant > epsilon:
        # Два различных корня
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [root1, root2]
    elif discriminant < -epsilon:
        # Нет корней
        return []
    else:
        # Один корень кратности два (дискриминант близок к нулю)
        root = -b / (2 * a)
        return [root]
