'''
This module tests generator_filter
'''
import unittest
import os
from itertools import islice
from generator_filter import gen


class TestJson(unittest.TestCase):
    def test_one_keyword(self):
        keywords = ["some"]
        file_data = ["some text", "in file", "for testing"]
        with open("test_file.txt", "w+") as outfile:
            outfile.write('\n'.join(map(str, file_data)))
        with open("test_file.txt", "r+") as outfile:
            res = gen(outfile, keywords)
            self.assertEqual(next(res), "some text\n")
        os.remove("test_file.txt")

    def test_as_in_lecture(self):
        file_data = ["A roza upala na lapu Azora"]
        with open("test_file.txt", "w+") as outfile:
            outfile.write('\n'.join(map(str, file_data)))
        with open("test_file.txt", "r+") as outfile:
            res = gen(outfile, ["roza"])
            self.assertEqual(next(res), "A roza upala na lapu Azora")
        with open("test_file.txt", "r+") as outfile:
            res = gen(outfile, ["roz"])
            self.assertEqual(next(res), None)
        with open("test_file.txt", "r+") as outfile:
            res = gen(outfile, ["rozan"])
            self.assertEqual(next(res), None)
        os.remove("test_file.txt")

    def test_registr(self):
        file_data = ["How it Works", "with Capital LetterS"]
        with open("test_file.txt", "w+") as outfile:
            outfile.write('\n'.join(map(str, file_data)))
        with open("test_file.txt", "r+") as outfile:
            res = gen(outfile, ["works"])
            self.assertEqual(next(res), "How it Works\n")
        with open("test_file.txt", "r+") as outfile:
            res = list(islice(gen(outfile, ["letters"]), 2))
            self.assertEqual(res[1], "with Capital LetterS")
        os.remove("test_file.txt")

    def test_more_keywords(self):
        file_data = ["Did i ever", "tell you", "the definition of", " ", "INSANITY?"]
        keywords = ["ever", "definition"]
        with open("test_file.txt", "w+") as outfile:
            outfile.write('\n'.join(map(str, file_data)))
        with open("test_file.txt", "r+") as outfile:
            res = list(islice(gen(outfile, keywords), 5))
            self.assertEqual(res[0], "Did i ever\n")
            self.assertEqual(res[1], None)
            self.assertEqual(res[2], "the definition of\n")
            self.assertEqual(res[3], None)
            self.assertEqual(res[4], None)
        os.remove("test_file.txt")

    def test_same_strings(self):
        file_data = ["it should be none", "this string has word science", "and this has Python"]
        keywords = ["science", "python"]
        with open("test_file.txt", "w+") as outfile:
            outfile.write('\n'.join(map(str, file_data)))
        with open("test_file.txt", "r+") as outfile:
            res = list(islice(gen(outfile, keywords), 3))
            self.assertEqual(res[0], None)
            self.assertEqual(res[1], "this string has word science\n")
            self.assertEqual(res[2], "and this has Python")
        os.remove("test_file.txt")

    def test_some_keywords_in_string(self):
        file_data = ["this string has two keywors", "some text"]
        keywords = ["has", "two"]
        with open("test_file.txt", "w+") as outfile:
            outfile.write('\n'.join(map(str, file_data)))
        with open("test_file.txt", "r+") as outfile:
            res = list(islice(gen(outfile, keywords), 2))
            self.assertEqual(res[0], "this string has two keywors\n")
            self.assertEqual(res[1], None)
        os.remove("test_file.txt")
