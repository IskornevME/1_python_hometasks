'''
This module tests read_write_cls
'''
import os
import unittest
from read_write_cls import read_data, dump_data,\
    JsonReader, JsonWriter, TxtReader, TxtWriter,\
    CsvReader, CsvWriter


class TestJson(unittest.TestCase):
    def test_json_short(self):
        data = {"x": "y"}
        with open("test_file.json", "w+") as outfile:
            dump_data(data, outfile, writer=JsonWriter())
        with open("test_file.json", "r+") as infile:
            res = read_data(infile, reader=JsonReader())
        self.assertEqual(res, data)
        os.remove("test_file.json")

    def test_json_long(self):
        data = {"name": "Ivan", "age": 37,
                "mother": {"name": "Olga", "age": 58}, "children": "Masha"}
        with open("test_file.json", "w+") as outfile:
            dump_data(data, outfile, writer=JsonWriter())
        with open("test_file.json", "r+") as infile:
            res = read_data(infile, reader=JsonReader())
        self.assertEqual(res, data)
        os.remove("test_file.json")

    def test_empty_dict(self):
        data = {}
        with open("test_file.json", "w+") as outfile:
            dump_data(data, outfile, writer=JsonWriter())
        with open("test_file.json", "r+") as infile:
            res = read_data(infile, reader=JsonReader())
        self.assertEqual(res, data)
        os.remove("test_file.json")


class TestTxt(unittest.TestCase):
    def test_txt_short(self):
        data = ["I love python intensive"]
        with open("test_file.txt", "w+") as outfile:
            dump_data(data, outfile, writer=TxtWriter())
        with open("test_file.txt", "r+") as infile:
            res = read_data(infile, reader=TxtReader())
        self.assertEqual(res, data)
        os.remove("test_file.txt")

    def test_txt_long(self):
        data = ["did I ever", "tell you", "the definition of", "INSANITY?"]
        with open("test_file.txt", "w+") as outfile:
            dump_data(data, outfile, writer=TxtWriter())
        with open("test_file.txt", "r+") as infile:
            res = read_data(infile, reader=TxtReader())
        self.assertEqual(res, data)
        os.remove("test_file.txt")

    def test_empty_list(self):
        data = []
        with open("test_file.txt", "w+") as outfile:
            dump_data(data, outfile, writer=TxtWriter())
        with open("test_file.txt", "r+") as infile:
            res = read_data(infile, reader=TxtReader())
        self.assertEqual(res, data)
        os.remove("test_file.txt")


class TestCsv(unittest.TestCase):
    def test_csv_short(self):
        data = [["Name"], ["Messi"]]
        with open("test_file.csv", "w+") as outfile:
            dump_data(data, outfile, writer=CsvWriter())
        with open("test_file.csv", "r+") as infile:
            res = read_data(infile, reader=CsvReader())
        self.assertEqual(res, data)
        os.remove("test_file.csv")

    def test_txt_long(self):
        data = [["Name", "Team", "Age", "Country"],
                ["Messi", "PSG", "35", "Argentina"],
                ["Lewandowski", "Barcelona", "34", "Poland"]]
        with open("test_file.csv", "w+") as outfile:
            dump_data(data, outfile, writer=CsvWriter())
        with open("test_file.csv", "r+") as infile:
            res = read_data(infile, reader=CsvReader())
        self.assertEqual(res, data)
        os.remove("test_file.csv")

    def test_empty_list(self):
        data = [[]]
        with open("test_file.csv", "w+") as outfile:
            dump_data(data, outfile, writer=CsvWriter())
        with open("test_file.csv", "r+") as infile:
            res = read_data(infile, reader=CsvReader())
        self.assertEqual(res, data)
        os.remove("test_file.csv")
