def ev_odd(nums):
    even = []
    odd = []
    for elem in nums:
        if elem % 2 == 0:
            even.append(elem)
        else:
            odd.append(elem)
    return (even, odd)

assert ev_odd([1, 2 , 3, 4, 5]) == ([2, 4], [1, 3, 5])
assert ev_odd([200, 777, 32, 57, 4, 5, -6, -9]) == ([200, 32, 4, -6], [777, 57, 5, -9])
assert ev_odd([-7, 5, -3, -3, -3, 0, 765, 200540]) == ([0, 200540], [-7, 5, -3, -3, -3, 765])