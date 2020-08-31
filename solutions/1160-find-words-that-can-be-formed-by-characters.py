"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.


"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sol = 0
        counter = dict()
        for char in chars:
            if  char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        for word in words:
            n = len(word)
            sol += n
            counter_word = dict()
            for el in word:
                if el not in counter:
                    sol -= n
                    break
                else:
                    if el not in counter_word:
                        counter_word[el] = 1
                    else:
                        counter_word[el] += 1
                        if counter_word[el] > counter[el]:
                            sol -= n
                            break
        return sol
