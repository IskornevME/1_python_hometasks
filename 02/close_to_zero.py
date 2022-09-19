from math import fabs

def close_to_zero(nums):
    dct = {}
    min_ = fabs(nums[0])
    for i in nums:
        dct[i] = fabs(i)
        if dct[i] < min_:
            min_ = dct[i]
    a = []
    for i in nums:
        if dct[i] <= min_:
            a.append(i)
    return a


assert close_to_zero([-1, 2, -5, 1, 1, -0.0001, -1, 0.9]) == [-0.0001]
assert close_to_zero([-5, 9, 6, -8]) == [-5]
assert close_to_zero([-1, 2, -5, 1, -1]) == [-1, 1, -1]
assert close_to_zero([-1, 0.5, -5, 2, -0.5, 4, 14022, -777, 0.50001, 0.5]) == [0.5, -0.5, 0.5]