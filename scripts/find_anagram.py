"""Python script create lists of anagrams from a list of words

What is Anagram?
    A word, phrase, or name formed by rearranging the letters of
another, such as spar, formed from rasp.
"""
__author__ = 'me@kartheek.net (Karnati Kartheek)'

from collections import Counter


def get_anagrams(word, anagrams):
    return filter(lambda anagram: Counter(word) == Counter(anagram), anagrams)
