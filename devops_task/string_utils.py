#some comments for branches
def print_string(value) -> None:
    if not isinstance(value, str):
        print("Помилка! Приймає текст")
        return
    print(value)


def analyze_string_case(value):
    if not isinstance(value, str):
        print("Помилка! Приймає текст")
        return None

    if value.isupper():
        return "Всі літери великі"
    if value.islower():
        return "Всі літери малі"
    return "Регістр заміксований"


def uppercase_letters_list(word):
    if not isinstance(word, str):
        print("Помилка! Приймає текст")
        return None

    return [ch.upper() for ch in word]
