# misol linki    https://www.codewars.com/kata/5f8a15c06dbd530016be0c19/train/python


def duplicate_sandwich(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) == 2:
            first_occurrence = i
            break

    second_occurrence = lst.index(lst[first_occurrence], first_occurrence + 1)

    return lst[first_occurrence + 1:second_occurrence]


print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))
print(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']))
print(duplicate_sandwich([0, 0]))
print(duplicate_sandwich([True, False, True]))
print(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']))
