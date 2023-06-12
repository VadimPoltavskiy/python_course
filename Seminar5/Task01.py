def replacement_mark (lists):
    print(lists)
    minimal = min(lists)
    maximal = max(lists)
    for i in range(len(lists)):
        if lists[i] == maximal:
            lists[i] = minimal
    print(lists)

mark = [5, 5, 4, 3, 2, 3, 2, 1, 2, 3, 3, 4, 3, 5]
replacement_mark(mark)