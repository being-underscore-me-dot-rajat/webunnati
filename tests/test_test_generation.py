import unittest
from pathlib import Path

from test_generation import discover_edge_cases, generate_test_module, optimize_coverage


class TestGenerationTests(unittest.TestCase):
    def test_discover_edge_cases_contains_division_by_zero(self):
        cases = discover_edge_cases()
        self.assertTrue(any(case["name"] == "divide_by_zero" for case in cases))

    def test_generate_test_module_creates_file(self):
        output_path = Path("tests/generated_snapshot.py")
        generated = generate_test_module(discover_edge_cases(), output_path)
        self.assertTrue(generated.exists())
        self.assertIn("class GeneratedEdgeCaseTests", generated.read_text())
        generated.unlink(missing_ok=True)

    def test_optimize_coverage_recommends_missing_cases(self):
        cases = discover_edge_cases()
        report = optimize_coverage(cases, Path("calculator.py"))
        self.assertIn("missing", report)
        self.assertTrue(any("division by zero" in item.lower() for item in report["missing"]))


if __name__ == "__main__":
    unittest.main()
