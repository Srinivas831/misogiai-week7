from collections import Counter

class TextAnalyzer:
    def __init__(self, text):
        """
        Initialize with text to analyze
        """
        self.original_text = text
        self.text = text.lower()  # For case-insensitive analysis

    def get_character_frequency(self, include_spaces=False):
        """
        Get frequency of each character
        Args:
            include_spaces (bool): Whether to include spaces in count
        Returns:
            Counter: Character frequencies
        """
        cleaned_text = self.text if include_spaces else self.text.replace(" ", "")
        return Counter(cleaned_text)

    def get_word_frequency(self, min_length=1):
        """
        (To be implemented)
        """
        pass

    def get_sentence_length_distribution(self):
        """
        (To be implemented)
        """
        pass

    def find_common_words(self, n=10, exclude_common=True):
        """
        (To be implemented)
        """
        pass

    def get_reading_statistics(self):
        """
        (To be implemented)
        """
        pass

    def compare_with_text(self, other_text):
        """
        (To be implemented)
        """
        pass



sample_text = """
Python is a high-level, interpreted programming language with dynamic semantics.
Its high-level built-in data structures, combined with dynamic typing and dynamic binding,
make it very attractive for Rapid Application Development. Python is simple, easy to learn
syntax emphasizes readability and therefore reduces the cost of program maintenance.
Python supports modules and packages, which encourages program modularity and code reuse.
The Python interpreter and the extensive standard library are available in source or binary
form without charge for all major platforms, and can be freely distributed.
"""

analyzer = TextAnalyzer(sample_text)
print("Character frequency (top 5):", analyzer.get_character_frequency().most_common(5))

