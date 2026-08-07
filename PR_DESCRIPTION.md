# PR Title
Add calculator demo and pytest coverage

# PR Summary
This pull request introduces a simple Python calculator demo and a pytest-based test suite to exercise its core arithmetic functions and common runtime error scenarios. It also adds basic usage documentation so the repository is easier to run and validate.

# What Changed
- Added a lightweight calculator demo in [demo.py](demo.py) with functions for add, subtract, multiply, divide, power, and a small demonstration runner.
- Added a pytest suite in [test_demo.py](test_demo.py) covering arithmetic behavior and expected runtime failures such as type errors, division by zero, and undefined names.
- Added setup/run instructions in [README.md](README.md) for running tests locally.

# Why This Change
The repository now has a clearer example of Python behavior for arithmetic operations and failure handling, along with automated checks to verify expected outcomes.

# Testing
Run the following locally:

```bash
pytest -q
```

# Review Suggestions
- Confirm that the calculator demo is intentionally simple and appropriate for the repository’s purpose.
- Review whether the error-demo behavior in [demo.py](demo.py) is meant for educational use or should be moved into a dedicated examples file.
- Check that the test coverage in [test_demo.py](test_demo.py) adequately reflects the intended behavior without being overly broad.

# Optional Short Version
Adds a simple calculator demo and accompanying pytest tests to provide a working example and basic regression coverage for arithmetic operations and runtime errors.
