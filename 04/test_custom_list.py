'''
Tests for Customlist
'''
from class_custom_list import Customlist



a = Customlist([1, 2, 3, 4, 5])
b = Customlist([3, 5])
test_lst = [100, 200, 300]

c = a + b
true_res = [4, 7, 3, 4, 5]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert b == [3, 5]
assert a == [1, 2, 3, 4, 5]

c = b + a
true_res = [4, 7, 3, 4, 5]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert b == [3, 5]
assert a == [1, 2, 3, 4, 5]

c = a + test_lst
true_res = [101, 202, 303, 4, 5]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert test_lst == [100, 200, 300]
assert a == [1, 2, 3, 4, 5]

c = test_lst + a
true_res = [101, 202, 303, 4, 5]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert test_lst == [100, 200, 300]
assert a == [1, 2, 3, 4, 5]

c = b + test_lst
true_res = [103, 205, 300]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert b == [3, 5]
assert test_lst == [100, 200, 300]

c = test_lst + b
true_res = [103, 205, 300]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert test_lst == [100, 200, 300]
assert b == [3, 5]

a += [9, 10, 11]
true_res = [10, 12, 14, 4, 5] 
for i in range(len(true_res)):
    assert a[i] == true_res[i]

b += [9, 10, 11]
true_res = [12, 15, 11]
for i in range(len(true_res)):
    assert b[i] == true_res[i]


    
a = Customlist([1, 2, 3, 4, 5])
b = Customlist([3, 5])
test_lst = [100, 200, 300]

c = a - b
true_res = [-2, -3, 3, 4, 5]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert isinstance(a - b, Customlist)
assert b == [3, 5]
assert a == [1, 2, 3, 4, 5]

c = b - a
true_res = [2, 3, -3, -4, -5]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert b == [3, 5]
assert a == [1, 2, 3, 4, 5]

c = a - test_lst
true_res = [-99, -198, -297, 4, 5]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert test_lst == [100, 200, 300]
assert a == [1, 2, 3, 4, 5]

c = test_lst - a
true_res = [99, 198, 297, -4, -5]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert test_lst == [100, 200, 300]
assert a == [1, 2, 3, 4, 5]

c = b - test_lst
true_res = -97, -195, -300
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert b == [3, 5]
assert test_lst == [100, 200, 300]

c = test_lst - b
true_res = [97, 195, 300]
for i in range(len(true_res)):
    assert c[i] == true_res[i]
assert b == [3, 5]
assert test_lst == [100, 200, 300]

a -= [9, 10, 11]
true_res = [-8, -8, -8, 4, 5]
for i in range(len(true_res)):
    assert a[i] == true_res[i]

b -= [9, 10, 11]
true_res = [-6, -5, -11]
for i in range(len(true_res)):
    assert b[i] == true_res[i]



a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a == b) is False
assert (a == test_lst) == False
assert (a == [1, 2, 3, 4, 5]) == True
assert (a == [sum([1, 2, 3, 4, 5])]) == True
assert (b == [2, 2, 2, 2]) == True



a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a != b) == True
assert (a != test_lst) == True
assert (a != [1, 2, 3, 4, 5]) == False
assert (a != [sum([1, 2, 3, 4, 5])]) == False
assert (b != [2, 2, 4]) == False



a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a < b) == False
assert (a < test_lst) == True
assert (test_lst < b) == False
assert (a < [16]) == True
assert (a < [1, 1]) == False



a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a > b) == True
assert (a > test_lst) == False
assert (test_lst > b) == True
assert (a > [16]) == False
assert (a > [1, 1]) == True



a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a <= b) == False
assert (a <= test_lst) == True
assert (test_lst <= b) == False
assert(a <= [15]) == True
assert (a < [15]) == False
assert (a <= [1, 1]) == False
assert(b <= [4, 4]) == True
assert (b < [4, 4]) == False



a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a >= b) == True
assert (a >= test_lst) == False
assert (test_lst >= b) == True
assert (a >= [15]) == True
assert (a > [15]) == False
assert(b >= [4, 4]) == True
assert (b > [4, 4]) == False


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert str(a) == '([1, 2, 3, 4, 5], 15)'
assert str(b) == '([3, 5], 8)'
