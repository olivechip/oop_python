"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Obtains a random word from a given file

    >>> w = WordFinder('words.txt')
    235891 words read

    """
    def __init__(self, file_path):
        """Reads file and prints # of words"""
        file = open(file_path, 'r')
        self.word_list = self.get_words(file)
        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        return str(self.word_list)

    def get_words(self, file):
        """Creates list of words"""
        return [word.strip() for word in file]

    def random(self):
        """Returns a random word"""
        return random.choice(self.word_list)

class SpecialWordFinder(WordFinder):
    """Obtains a random word from a given file, excluding blanks and comments

    >>> w = SpecialWordFinder('words.txt')
    235886 words read

    """
    def get_words(self, file):
        """Creates list of words, excluding blanks and comments"""
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]
