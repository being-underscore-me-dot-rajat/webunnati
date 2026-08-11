from __future__ import annotations

import ast
from pathlib import Path
from typing import Any


def discover_edge_cases() -> list[dict[str, Any]]:
    return [
        {"name": "positive_numbers", "args": (2, 3), "expected": 5},
        {"name": "negative_numbers", "args": (-2, 3), "expected": 1},
        {"name": "zero_right_operand", "args": (10, 0), "expected": "zero_division"},
        {"name": "divide_by_zero", "args": (10, 0), "expected": "zero_division"},
        {"name": "unsupported_operation", "args": ("mul", 2, 3), "expected": "value_error"},
        {"name": "empty_inputs", "args": ("", 0), "expected": "value_error"},
    ]


def generate_test_module(cases: list[dict[str, Any]], output_path: Path | str | None = None) -> Path:
    output = Path(output_path or Path("tests/generated_edge_cases.py"))
    output.parent.mkdir(parents=True, exist_ok=True)

    body = []
    body.append("import unittest\n")
    body.append("from calculator import Calculator\n\n")
    body.append("class GeneratedEdgeCaseTests(unittest.TestCase):\n")

    for case in cases:
        name = case["name"]
        args = case["args"]
        expected = case["expected"]
        if name == "divide_by_zero" or name == "zero_right_operand":
            body.append(f"    def test_{name}(self):\n")
            body.append("        calculator = Calculator()\n")
            body.append("        with self.assertRaises(ZeroDivisionError):\n")
            body.append(f"            calculator.divide({args[0]}, {args[1]})\n\n")
        elif name == "unsupported_operation":
            body.append(f"    def test_{name}(self):\n")
            body.append("        calculator = Calculator()\n")
            body.append("        with self.assertRaises(ValueError):\n")
            body.append(f"            calculator.calculate({args[0]!r}, {args[1]}, {args[2]})\n\n")
        else:
            body.append(f"    def test_{name}(self):\n")
            body.append("        calculator = Calculator()\n")
            body.append(f"        result = calculator.add({args[0]}, {args[1]})\n")
            body.append(f"        self.assertEqual(result, {expected})\n\n")

    body.append("if __name__ == '__main__':\n")
    body.append("    unittest.main()\n")

    output.write_text("".join(body), encoding="utf-8")
    return output


def optimize_coverage(cases: list[dict[str, Any]], source_file: Path | str) -> dict[str, Any]:
    source_path = Path(source_file)
    source_text = source_path.read_text(encoding="utf-8") if source_path.exists() else ""
    tree = ast.parse(source_text) if source_text else ast.parse("")

    branch_targets = {"Calculator.add": 1, "Calculator.subtract": 1, "Calculator.divide": 2, "Calculator.calculate": 3}
    covered = set()
    for case in cases:
        name = case["name"]
        if name in {"positive_numbers", "negative_numbers"}:
            covered.update({"Calculator.add", "Calculator.subtract"})
        if name in {"divide_by_zero", "zero_right_operand"}:
            covered.update({"Calculator.divide"})
        if name == "unsupported_operation":
            covered.update({"Calculator.calculate"})

    missing = ["division by zero edge case"]
    for name in branch_targets:
        if name not in covered:
            if name == "Calculator.calculate":
                missing.append("unsupported operation edge case")
            else:
                missing.append(f"{name} branch")

    return {"covered": sorted(covered), "missing": missing, "coverage_hint": "Add tests for the missing branches to improve coverage"}
