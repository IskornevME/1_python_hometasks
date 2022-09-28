'''
Tests for Customlist
'''
from class_custom_list import Customlist


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a + b).lst == [4, 7, 3, 4, 5]
assert isinstance(a + b, Customlist)
assert b.lst == [3,5]

assert (b + a).lst == [4, 7, 3, 4, 5]
assert b.lst == [3,5]

assert (a + test_lst).lst == [101, 202, 303, 4, 5]
assert test_lst == [100, 200, 300]

assert (test_lst + a).lst == [101, 202, 303, 4, 5]
assert test_lst == [100, 200, 300]

assert (b + test_lst).lst == [103, 205, 300]
assert b.lst == [3, 5]

assert (test_lst + b).lst == [103, 205, 300]
assert b.lst == [3, 5]

a += [9, 10, 11]
assert a.lst == [10, 12, 14, 4, 5]
b += [9, 10, 11]
assert b.lst == [12, 15, 11]


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert(a - b).lst == [-2, -3, 3, 4, 5]
assert isinstance(a - b, Customlist)
assert b.lst == [3,5]

assert(b - a).lst == [2, 3, -3, -4, -5]
assert b.lst == [3,5]

assert (a - test_lst).lst == [-99, -198, -297, 4, 5]
assert test_lst == [100, 200, 300]

assert (test_lst - a).lst == [99, 198, 297, -4, -5]
assert test_lst == [100, 200, 300]

assert (b - test_lst).lst == [-97, -195, -300]
assert b.lst == [3, 5]

assert (test_lst - b).lst == [97, 195, 300]
assert b.lst == [3, 5]

a -= [9, 10, 11]
assert a.lst == [-8, -8, -8, 4, 5]
b -= [9, 10, 11]
assert b.lst == [-6, -5, -11]


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a == b) is False
assert (a == test_lst) is False
assert (a == [1, 2, 3, 4, 5]) is True
assert (a == [sum([1, 2, 3, 4, 5])]) is True
assert (b == [2, 2, 2, 2]) is True


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a != b) is True
assert (a != test_lst) is True
assert (a != [1, 2, 3, 4, 5]) is False
assert (a != [sum([1, 2, 3, 4, 5])]) is False
assert (b != [2, 2, 4]) is False


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a < b) is False
assert (a < test_lst) is True
assert (test_lst < b) is False
assert (a < [16]) is True
assert (a < [1, 1]) is False


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a > b) is True
assert (a > test_lst) is False
assert (test_lst > b) is True
assert (a > [16]) is False
assert (a > [1, 1]) is True


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a <= b) is False
assert (a <= test_lst) is True
assert (test_lst <= b) is False
assert(a <= [15]) is True
assert (a < [15]) is False
assert (a <= [1, 1]) is False
assert(b <= [4, 4]) is True
assert (b < [4, 4]) is False


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert (a >= b) is True
assert (a >= test_lst) is False
assert (test_lst >= b) is True
assert (a >= [15]) is True
assert (a > [15]) is False
assert(b >= [4, 4]) is True
assert (b > [4, 4]) is False


a = Customlist([1,2, 3, 4, 5])
b = Customlist([3,5])
test_lst = [100, 200, 300]

assert str(a) == '([1, 2, 3, 4, 5], 15)'
assert str(b) == '([3, 5], 8)'
