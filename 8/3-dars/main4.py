# misol linki    https://www.codewars.com/kata/54466996990c921f90000d61/train/python

def is_monotone(heights):
    if not heights:
        return True
    return all(heights[i] <= heights[i + 1] for i in range(len(heights) - 1))

print(is_monotone([1, 2, 3]))
print(is_monotone([1, 1, 2]))
print(is_monotone([1]))
print(is_monotone([3, 2, 1]))
print(is_monotone([3, 2, 2]))
print(is_monotone([]))
