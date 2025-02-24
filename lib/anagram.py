# your code goes here!

class Anagram:
    def __init__(self, anagram):
        self.anagram = anagram.lower()

    def match(self, words):
        main_sorted = sorted(self.anagram)

        matching_words = [word for word in words if sorted(word.lower()) == main_sorted]

        return matching_words


word1 = Anagram("enlist")
print(word1.match(["listen", "poison", "hello"]))
