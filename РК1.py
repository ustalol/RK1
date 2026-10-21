INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_outcode(x, y, x_min, y_min, x_max, y_max):

    code = INSIDE

    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT

    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP

    return code



X_MIN, Y_MIN = 10, 10
X_MAX, Y_MAX = 50, 50

points = [
    (30, 30),
    (5, 30),
    (55, 55),
    (30, 2)
]

print(f"Границы окна: X[{X_MIN}, {X_MAX}], Y[{Y_MIN}, {Y_MAX}]\n")
print(f"{'Точка':<10} | {'Код (Десятичный)':<17} | {'Код (Двоичный)':<15}")
print("-" * 50)

for x, y in points:
    outcode = compute_outcode(x, y, X_MIN, Y_MIN, X_MAX, Y_MAX)

    binary_code = f"{outcode:04b}"
    print(f"({x:>2}, {y:>2})     | {outcode:<17} | {binary_code:<15}")
