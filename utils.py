from num2words import num2words

def sort_number_words(numbers):
    return sorted([num2words(n) for n in numbers])
