'''
This file tests function fing_anagrams
'''
import unittest
from unittest.mock import patch
from io import StringIO
import find_anagrams


class TestAnagrams(unittest.TestCase):
    def test_input(self):
        '''
        Check that out function validate_input works correctly
        '''
        with patch('sys.stdout', new=StringIO()):
            res = find_anagrams.find_anagrams("s!nT", "n")
            self.assertEqual(res, 0)
            res = find_anagrams.find_anagrams("abcbca", "BC")
            self.assertEqual(res, 0)
            res = find_anagrams.find_anagrams("", "")
            self.assertEqual(res, 0)
            res = find_anagrams.find_anagrams("abcd", "")
            self.assertEqual(res, 0)
            res = find_anagrams.find_anagrams("", "ab")
            self.assertEqual(res, 0)

    def test_in_task(self):
        '''
        Check that tests from lecture is working
        '''
        res = find_anagrams.find_anagrams("abcba", "abc")
        self.assertEqual(res, [0, 2])
        res = find_anagrams.find_anagrams("aaa", "a")
        self.assertEqual(res, [0, 1, 2])
        res = find_anagrams.find_anagrams("abc cba xabcd", "abc")
        self.assertEqual(res, [0, 4, 9])

    def test_no_pat_in_txt(self):
        '''
        Check that if text has no pattern we get empty list
        '''
        res = find_anagrams.find_anagrams("qwerty", "a")
        self.assertEqual(res, [])
        res = find_anagrams.find_anagrams("some text for test", "glnk")
        self.assertEqual(res, [])

    def test_first_and_last_letter(self):
        '''
        Check that bound cases works correctly
        '''
        text = "givikjvevia"
        res = find_anagrams.find_anagrams(text, "a")
        self.assertEqual(res, [len(text) - 1])
        res = find_anagrams.find_anagrams("agivikjvevi", "a")
        self.assertEqual(res, [0])
        res = find_anagrams.find_anagrams("abdl gsvs fesccrf", "abdl")
        self.assertEqual(res, [0])

    def test_my_cases(self):
        '''
        Check my own cases
        '''
        res = find_anagrams.find_anagrams("ababababa", "ab")
        self.assertEqual(res, [0, 1, 2, 3, 4, 5, 6, 7])
        res = find_anagrams.find_anagrams("ababababa", "a")
        self.assertEqual(res, [0, 2, 4, 6, 8])
        text = "abcd  ncbadbc a b c d cbad  "
        res = find_anagrams.find_anagrams(text, "abcd")
        self.assertEqual(res, [0, 7, 9, 22])
