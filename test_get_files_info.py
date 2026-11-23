from functions.get_files_info import get_files_info

success = "Success:"

# Current directory
r = get_files_info("calculator", ".")
# print("Results for current directory:\n" + "\n".join(output_list))
print("Results for current directory:\n" + r)

r = get_files_info("calculator", "pkg")
print("Results for current directory:\n" + r)

# Bin directory
r = get_files_info("calculator", "/bin")
print("Results for current directory:\n" + r)

# Parent directory
r = get_files_info("calculator", "../")
print("Results for current directory:\n" + r)

