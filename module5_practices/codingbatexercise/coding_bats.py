def warmup1(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


def warmup2(n):
    for x in range(0, len(n) + 1):
        result += n[:x]
    return result


def string2(n):
    count_cat = 0
    count_dog = 0
    for i in range(len(n) - 2):
        if n[i : i + 3] == "dog":
            count_dog += 1
        if n[i : i + 3] == "cat":
            count_cat += 1


def logic2(a, b, c):
    if a == b == c:
        result = 0
    if b == c:
        result = a
    if a == c:
        result = b
    if a == b:
        result = c
    else:
        result = a + b + c
    return result
