# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

    def match(self, word_list):
        anagrams = []
        for candidate in word_list:
            # Check if the candidate word is not the same as the original word and has the same letters
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted(self.word):
                anagrams.append(candidate)
        return anagrams
