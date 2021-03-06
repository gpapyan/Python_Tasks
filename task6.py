"""
6.	A one-dimensional list of natural numbers is given. Sort the given list in ascending order of the sum of the
digits. For example, an array of numbers is given [14, 30, 103]. After sorting it will be like this: [30, 103, 14],
because the sum of the digits of 30 is 3, the number 103 is 4, and the number 14 is 5.

"""


def sort(num):
    elements = [int(elem) for elem in str(num)]
    return sum(elements)


lst = [38, 15, 64, 30, 55, 30, 103]
print(sorted(lst, key=sort))


# Noric Grel aranc buildin methodneri

def num_sort(nums):
    unordered = nums.copy()
    ordered = []
    while unordered:
        smallest = unordered[0]
        s = sum(int(c) for c in str(smallest) if c != "-")
        for t in unordered:
            t_s = sum(int(c) for c in str(t) if c != "-")
            if t_s < s:
                smallest = t
                s = t_s
        ordered.append(smallest)
        unordered.remove(smallest)
    return ordered


lst = [38, 15, 64, 30, 55, 30, 103]

print(num_sort(lst))
