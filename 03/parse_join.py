import json
import string


def word_count(st, word):
    st = st.translate(str.maketrans('', '', string.punctuation))
    st = st.lower().split(' ')
    dct = {}
    dct[word] = 0
    for el in st:
        if el in dct:
            dct[el] += 1
        else:
            dct[el] = 1
    return dct[word]


def parse_json(keyword_callback, json_str: str, required_fields=None, keywords=None):
    count = 0
    json_doc = json.loads(json_str)
    if len(required_fields) == 0 or len(keywords) == 0:
        print('Fields or keywors are not specified')
        return -1
    num_miss_fields = 0
    
    for field in required_fields:
        if field not in json_doc.keys():
            print('There is no fields in string:', field)
            num_miss_fields += 1
        else:
            for i in range(len(keywords)):
                count = word_count(json_doc[field], keywords[i])
                if count > 0:
                    for k in range(count):
                        keyword_callback(field, keywords[i], dct)
                
    if num_miss_fields == len(required_fields):
        print("Strind doesn't have required fields")
        return -1


def keyword_callback(field, st, dct):
    new_key = field + ' - ' + st
    if new_key in dct.keys():
        dct[new_key] += 1
    else:
        dct[new_key] = 1
        

dct = dict()
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
parse_json(keyword_callback, json_str, ['key1'], ["word2"])
assert dct == {'key1 - word2': 1}

dct.clear()
json_str = '{"key1": "Word1 word2 word3", "key2": "word2 word3", "key3": "word1 word2 word3 word4"}'
parse_json(keyword_callback, json_str, ["ddd", "fff", "key1", "key3", "key"], ["word2", "word4"])
assert dct == {'key1 - word2': 1, 'key3 - word2': 1, 'key3 - word4': 1}

dct.clear()
json_str = '{"key1": "Word1 word2, word3 word2 word4less", "key3": "word2 word3 word4!"}'
parse_json(keyword_callback, json_str, ['ddd', 'fff', 'key1', 'key3'], ["word2", "word4"])
assert dct == {'key1 - word2': 2, 'key3 - word2': 1, 'key3 - word4': 1}

dct.clear()
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
assert parse_json(keyword_callback, json_str, [], ["word2"]) == -1

dct.clear()
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
assert parse_json(keyword_callback, json_str, ["key2"], []) == -1

dct.clear()
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
assert parse_json(keyword_callback, json_str, ["dvgs", "drgd"], ["word2"]) == -1