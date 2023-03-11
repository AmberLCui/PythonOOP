"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Finds random words in dictionary.

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True

    >>> wf.random() in wf.words
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read"""

        with open(path) as dict_file:
            self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        if not self.words:
            raise ValueError("The list of words is empty")
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in swf.words
    True

    >>> swf.random() in swf.words
    True

    >>> swf.random() in swf.words
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]


wf_instance = WordFinder("simple.txt")
swf_instance = SpecialWordFinder("complex.txt")
