#generator, that sends Even then Odd
def even_odd_words():
    i = 0
    while True:
        if i % 2 == 0:
            yield "Парне"
        else:
            yield "Непарне"
        i += 1
