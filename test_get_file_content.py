from functions.get_files_info import get_file_content

success = "Success:"

# Current directory
r = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(r)}")
print(f"lorem.txt truncated: {'truncated' in r}")

# r1 = get_file_content("calculator", "main.py")
# # print(f"calculator.py length: {len(r1)}")
# print(r1)

# r1 = get_file_content("calculator", "pkg/calculator.py")
# # print(f"calculator.py length: {len(r1)}")
# print(r1)

# r2 = get_file_content("calculator", "/bin/cat")
# print(r2)

# r3 = get_file_content("calculator", "pkg/does_not_exist.py")
# print(r3)