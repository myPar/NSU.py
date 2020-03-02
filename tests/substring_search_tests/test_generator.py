import random


def test_str_generator(lib: str, string_len: int, substring_len: int) -> str:   # generate string and substring using symbols from lib
    test_str = ""
    test_sub_str = ""

    for i in range(string_len):
        rand_idx = random.randint(0, len(lib) - 1)
        test_str += lib[rand_idx]

    for i in range(substring_len):
        rand_idx = random.randint(0, len(lib) - 1)
        test_sub_str += lib[rand_idx]

    return test_str + " " + test_sub_str


def generator(line_number: int, lib: str, string_len: int, substring_len: int):     # writes test strings in file tests_data
    tests_data = open("tests_data", 'w')

    for i in range(line_number):
        tests_data.write(test_str_generator(lib, string_len, substring_len) + '\n')
    tests_data.close()
