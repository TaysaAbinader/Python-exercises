def even_list(numbers):
    evens = []
    for n in numbers:
        if n %2 == 0:
            evens.append(n)
    return evens

list_int = range(10)
print(*list_int)
print(even_list(list_int))