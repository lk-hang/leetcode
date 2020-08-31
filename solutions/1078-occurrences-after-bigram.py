"""
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.
"""
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(' ')
        return [text[i+2] for i in range(len(text)-2) if text[i] == first and text[i+1] == second]
