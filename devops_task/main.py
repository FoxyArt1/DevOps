from devops_task.string_utils import print_string, analyze_string_case, uppercase_letters_list
from devops_task.parity_generator import even_odd_words


def run_examples():
    print("1) print_string")
    print_string("Привіт")

    print("\n2) analyze_string_case")
    print(analyze_string_case("HELLO"))
    print(analyze_string_case("hello"))
    print(analyze_string_case("HeLLo"))

    print("\n3) список літер smogtether у верхньому регістрі")
    print(uppercase_letters_list("smogtether"))

    print("\n4) генератор Парне і Непарне")
    gen = even_odd_words()
    for _ in range(6):
        print(next(gen))


if __name__ == "__main__":
    run_examples()
