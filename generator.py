import random

def load_words(file_path):
    """Load words from a given file into a list."""
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_random_words_sequence(words, length=10):
    """Generate a sequence of random words from the list."""
    return ' '.join(random.choices(words, k=length))


