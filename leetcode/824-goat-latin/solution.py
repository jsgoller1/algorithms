"""
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
"""


class Solution:
    def toGoatLatin(self, S):
        wordList = [list(word) for word in S.split(" ")]
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        # Word begins with consonant; drop first letter, append to end, add ma
        for i, word in enumerate(wordList):
            if word[0] not in vowels:
                word.append(word.pop(0))
            word += ["m", "a"]
            word += (["a"] * (i+1))
            wordList[i] = ''.join(word)
        return ' '.join(wordList)


if __name__ == '__main__':
    s = Solution()
    assert s.toGoatLatin("m") == "mmaa"
    assert s.toGoatLatin(
        "I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    assert s.toGoatLatin(
        "The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
