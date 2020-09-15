"""
Sums Problem
Given an array of integers, return the smallest set of indices of numbers such that 
they add up to a target number. You may not use the same element twice.

Examples:
[1,2,6,3,17,82,23,234] -> 26
Solution [3,6]

[1,2,6,3,17,82,23,234] -> 40
Solution [4,6]

[1,2,6,3,17,82,23,234] -> 23
Solution [6]
"""

def find_subset(arr, tg):
    # return the indecies
    def decomp(arr, n, tg, result=[]):
        # print(arr)
        # base case
        if n == 1:
            if arr[0][0] != tg:
                return []

        if arr[0][0] > tg:
            return decomp(arr[1:], n-1, tg, result)
        
        if arr[0][0] == tg:
            result.append(arr[0][1])
            return result

        if arr[0][0] < tg:
            temp = sorted([decomp(arr[1:], n-1, tg, result), decomp(arr[1:], n-1, tg-arr[0][0], result+[arr[0][1]])], key=len)
            return [i for i in temp if len(i) != 0]
    
    def flatten(f):
        if isinstance(f[0], int):
            return f
        elif len(f) == 1:
            return flatten(f[0])
        else:
            return [flatten(i) for i in f]

    arr = [[i, ipos] for ipos, i in enumerate(arr)]
    arr.sort(key=lambda x: x[0], reverse=True)
    result = decomp(arr, len(arr), tg)
    result = flatten(result)
    smallest_result = sorted(sorted(result, key=len)[0])
    return smallest_result


if __name__ == '__main__':
    # arr = [2,3,5,7,13]
    # tg = 23
    arr = [1,2,6,3,17,82,23,234]
    tg = 26
    print(find_subset(arr, tg))