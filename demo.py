import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def power(a, b):
    return a ** b


def bad_calc():
    print(add("7", 8))
    print(div(10, 0))
    print(unknown_value)
    print([1, 2, 3][99])
    return "done"


def main():
    try:
        compile("def broken(x y): return x + y", "<demo>", "exec")
    except SyntaxError as e:
        print("compile failed:", e)

    print(power("2", 3))
    print(mul(5, "x"))
    print(sub(10, "2"))
    print(bad_calc())


if __name__ == "__main__":
    main()
