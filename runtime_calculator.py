import tkinter as tk
from calculator import Calculator, CalculatorApp


class RuntimeCalculator(Calculator):
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


class RuntimeCalculatorApp(CalculatorApp):
    def __init__(self, root):
        super().__init__(root)
        self.calculator = RuntimeCalculator()
        self.root.title("Runtime Calculator")
        self.operation_var.set("divide")


def main():
    root = tk.Tk()
    app = RuntimeCalculatorApp(root)
    app.run()


if __name__ == "__main__":
    main()
