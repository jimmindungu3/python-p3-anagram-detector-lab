class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

    def match(self, possible_anagrams):
        # Use list comprehension to filter anagrams
        return [anagram for anagram in possible_anagrams if self.is_anagram(anagram)]

    def is_anagram(self, candidate):
        # Check if two words are anagrams by comparing sorted character lists
        return sorted(self.word) == sorted(candidate.lower())


