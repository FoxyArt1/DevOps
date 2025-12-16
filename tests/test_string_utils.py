from devops_task.string_utils import analyze_string_case, uppercase_letters_list, print_string


def test_analyze_string_case_upper():
    assert analyze_string_case("ABC") == "Всі літери великі"


def test_analyze_string_case_lower():
    assert analyze_string_case("abc") == "Всі літери малі"


def test_analyze_string_case_mixed():
    assert analyze_string_case("AbC") == "Регістр заміксований"


def test_uppercase_letters_list():
    assert uppercase_letters_list("smogtether") == list("SMOGTETHER")


def test_print_string_non_string_prints_error(capsys):
    print_string(123)
    out = capsys.readouterr().out
    assert "Помилка! Приймає текст" in out


def test_analyze_string_case_non_string_prints_error(capsys):
    result = analyze_string_case(123)
    out = capsys.readouterr().out
    assert result is None
    assert "Помилка! Приймає текст" in out
