
from functions.run_python_file import run_python_file

print("1. Running main.py:")
print(run_python_file("calculator", "main.py"))

print("\n2. Running calculator with arguments:")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\n3. Running tests.py:")
print(run_python_file("calculator", "tests.py"))

print("\n4. Testing outside working directory:")
print(run_python_file("calculator", "../main.py"))

print("\n5. Testing nonexistent file:")
print(run_python_file("calculator", "nonexistent.py"))

print("\n6. Testing non-Python file:")
print(run_python_file("calculator", "lorem.txt"))
