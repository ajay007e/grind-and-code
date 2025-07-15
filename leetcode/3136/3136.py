class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        has_vowel, has_consonant = False, False
        for char in word:
            if not has_vowel and char.lower() in vowels:
                has_vowel = True
            if not has_consonant and char.lower() in consonants:
                has_consonant = True
            if not char.isdigit() and not char.isalpha():
                return False
        return has_vowel and has_consonant
