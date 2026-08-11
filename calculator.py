import argparse
import sys
import tkinter as tk
from tkinter import ttk, messagebox


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def calculate(self, operation, a, b):
        normalized_op = operation.lower().strip()
        if normalized_op in {"add", "+"}:
            return self.add(a, b)
        if normalized_op in {"subtract", "sub", "-"}:
            return self.subtract(a, b)
        if normalized_op in {"divide", "div", "/"}:
            return self.divide(a, b)
        raise ValueError(f"Unsupported operation: {operation}")


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.calculator = Calculator()
        self.root.title("Calculator")
        self.root.geometry("360x220")
        self.root.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        self.operation_var = tk.StringVar(value="add")
        self.result_var = tk.StringVar(value="Result: ")

        ttk.Label(self.root, text="Left value:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.left_entry = ttk.Entry(self.root)
        self.left_entry.grid(row=0, column=1, padx=10, pady=8)

        ttk.Label(self.root, text="Right value:").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.right_entry = ttk.Entry(self.root)
        self.right_entry.grid(row=1, column=1, padx=10, pady=8)

        ttk.Label(self.root, text="Operation:").grid(row=2, column=0, padx=10, pady=8, sticky="w")
        operation_menu = ttk.Combobox(
            self.root,
            textvariable=self.operation_var,
            values=["add", "subtract", "divide"],
            state="readonly",
            width=15,
        )
        operation_menu.grid(row=2, column=1, padx=10, pady=8)

        ttk.Button(self.root, text="Calculate", command=self._on_calculate).grid(row=3, column=0, columnspan=2, pady=12)

        ttk.Label(self.root, textvariable=self.result_var, font=("Segoe UI", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=8)

    def _on_calculate(self):
        try:
            left = float(self.left_entry.get())
            right = float(self.right_entry.get())
            result = self.calculator.calculate(self.operation_var.get(), left, right)
            self.result_var.set(f"Result: {result}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.result_var.set("Result: error")
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))
            self.result_var.set("Result: error")

    def run(self):
        self.root.mainloop()


def run_cli(argv=None):
    parser = argparse.ArgumentParser(description="Simple object-oriented calculator")
    parser.add_argument("operation", choices=["add", "subtract", "divide"], help="Operation to perform")
    parser.add_argument("left", type=float, help="Left operand")
    parser.add_argument("right", type=float, help="Right operand")
    args = parser.parse_args(argv)

    calculator = Calculator()
    result = calculator.calculate(args.operation, args.left, args.right)
    print(result)
    return result


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if args:
        return run_cli(args)

    root = tk.Tk()
    app = CalculatorApp(root)
    app.run()
    return 0


if __name__ == "__main__":
    main()
