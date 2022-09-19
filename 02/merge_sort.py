import math
from collections import Counter

def merge_sort(lst, tp):
    B = []
    i = 0
    j = 0
    while i < len(lst)-1 and j < len(tp)-1:
        if math.isclose(lst[i], tp[j], rel_tol = 1e-9):
            B.append(lst[i])
            i += 1
            j += 1
        else:
            if lst[i] - tp[j] > 1e-9:
                j += 1
            if lst[i] - tp[j] < -1e-9:
                i += 1

    if j == len(tp)-1:
        for k in range(i, len(lst)):
            if math.isclose(lst[k], tp[j], rel_tol = 1e-9):
                B.append(lst[k])
                k += 1
            else:
                if lst[k] - tp[j] < -1e-9:
                    k += 1
        
    if i == len(lst)-1:
        for k in range(j, len(tp)):
            if math.isclose(lst[i], tp[k], rel_tol = 1e-9):
                B.append(tp[k])
                k += 1
            else:
                if lst[i] - tp[k] > 1e-9:
                    k += 1
                    
    res = Counter(B)
    return [i for i, fr in res.items()]

assert merge_sort([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]
assert merge_sort([0, 1, 1, 2, 3, 5, 7, 9, 9, 9],
                  (0, 1, 1, 2, 3, 4, 7, 9, 55)) == [0, 1, 2, 3, 7, 9]

assert merge_sort([-9, -0.5, 0, 5, 7, 976], 
                  (-11, -9, -1, 0, 6, 7, 954, 1000)) == [-9, 0, 7]