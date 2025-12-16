from devops_task.parity_generator import even_odd_words


def test_even_odd_words_sequence():
    gen = even_odd_words()
    assert next(gen) == "Парне"
    assert next(gen) == "Непарне"
    assert next(gen) == "Парне"
    assert next(gen) == "Непарне"
