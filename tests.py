from functions.get_files_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file


def tests():
    result = get_file_content("calculator", "pkg/render.py")
    print(result)

    result = get_files_info("calculator")
    print(result)

    resutl = run_python_file("calculator", "tests.py")
    print(resutl)

    result = write_file("calculator", "test.txt", "Hello, World!")
    print(result)


if __name__ == "__main__":
    tests()
