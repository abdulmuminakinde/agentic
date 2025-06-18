from functions.write_file import write_file


def tests():
    print(write_file("calculator", "lorem.txt", "Hello, world!"))
    print(write_file("calculator", "pkg/lorem.txt", "Hello, world!"))
    print(write_file("calculator", "../lorem.txt", "This should not be allowed"))


if __name__ == "__main__":
    tests()
