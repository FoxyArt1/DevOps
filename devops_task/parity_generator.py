#generator, that sends Even then Odd
def even_odd_words():
    even = True
    while True:
        yield "Парне" if even else "Непарне"
        even = not even