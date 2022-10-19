'''
In this module we made generator for filtering text
'''


def gen(fileobj, keywords):
    if len(keywords) == 0:
        print("Keywords are not specified")
        return
    for line in fileobj:
        tmp = line
        line = line.lower()
        line.strip()
        line = line.split()
        intersec = list(set(line) & set(keywords))
        if intersec:
            yield tmp
        else:
            yield None
