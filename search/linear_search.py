from array import array


def linear_search(haystack: array, needle: int) -> bool:
    for index, i in enumerate(haystack):
        if i == needle:
            return True
    return False

