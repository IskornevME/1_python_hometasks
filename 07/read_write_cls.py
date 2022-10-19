'''
This is module for reading and writing data in json, txt, csv
'''
import json
import csv


class BaseReader:
    @classmethod
    def read(cls, fileobj):
        pass


class BaseWriter:
    @classmethod
    def dump(cls, data, fileobj):
        pass


def read_data(fileobj, reader):
    return reader.read(fileobj)


def dump_data(data, fileobj, writer):
    writer.dump(data, fileobj)


class JsonReader(BaseReader):
    @classmethod
    def read(cls, fileobj):
        ans = json.load(fileobj)
        return ans


class JsonWriter(BaseReader):
    @classmethod
    def dump(cls, data, fileobj):
        json.dump(data, fileobj)


class TxtReader(BaseReader):
    @classmethod
    def read(cls, fileobj):
        ans = []
        line = fileobj.readline()
        while line:
            ans.append(line.strip())
            line = fileobj.readline()
        return ans


class TxtWriter(BaseWriter):
    @classmethod
    def dump(cls, data, fileobj):
        fileobj.write('\n'.join(map(str, data)))


class CsvReader(BaseReader):
    @classmethod
    def read(cls, fileobj):
        ans = csv.reader(fileobj, delimiter=',')
        res = []
        for line in ans:
            res.append(line)
        return res


class CsvWriter(BaseReader):
    @classmethod
    def dump(cls, data, fileobj):
        writer = csv.writer(fileobj, delimiter=',')
        for line in data:
            writer.writerow(line)
