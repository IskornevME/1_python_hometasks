'''
In this module we make function that finds anagrams in string
'''
def check(count_pat, count_text, alph_size):
    for j in range(alph_size):
        if count_text[j] != count_pat[j]:
            return 0
    return 1


def validate_input(text, pattern, arr_alph):
    all_inp = text + pattern
    if len(text) == 0 or len(pattern) == 0:
        print("Text or pattern is empty")
        return 0
    for elem in all_inp:
        if elem not in arr_alph:
            print("Please enter lowercase letters without punctuation marks")
            return 0
    return 1


def find_anagrams(text: str, pattern: str):
    alph_size = 27
    arr_alph = list('abcdefghijklmnopqrstuvwxyz ')
    alph_dic = {}
    for i in range(alph_size):
        alph_dic[arr_alph[i]] = i
    if not validate_input(text, pattern, arr_alph):
        return 0
    pat_size = len(pattern)
    count_pat = [0 for _ in range(alph_size)]
    count_text = [0 for _ in range(alph_size)]
    for i in range(pat_size):
        count_pat[alph_dic[pattern[i]]] += 1
        count_text[alph_dic[text[i]]] += 1
    idxs = []
    if check(count_pat, count_text, alph_size) == 1:
        idxs.append(0)

    for i in range(pat_size, len(text)):
        count_text[alph_dic[text[i - pat_size]]] -= 1
        count_text[alph_dic[text[i]]] += 1
        if check(count_pat, count_text, alph_size) == 1:
            idxs.append(i + 1 - pat_size)
    return idxs
