def showResultWithAttr(previous, start, target, attr='total_cost'):
    result = []
    curCity = target  # Truy vết từ điểm đích về điểm bắt đầu
    result.append(str(curCity))
    print('\nKết quả:', end=' ')

    while curCity != start:
        curCity = previous[curCity]['from']
        result.append(str(curCity))

    result = result[::-1]
    print(' -> '.join(result))


def showStep(counter, q, previous, attr='total_cost'):
    print('%d.' % counter, end=' ')
    i = 0
    lenQ = len(q)
    for v in q:
        i += 1
        if i < lenQ:
            print((previous[v]['from'], previous[v][attr], v), end=', ')
        else:
            print((previous[v]['from'], previous[v][attr], v))


def aweSomeSort(array, previous, sortBy='total_cost'):  # QuickSort (python version)
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = previous[array[0]][sortBy]
        for city in array:
            cost = previous[city][sortBy]
            if cost < pivot:
                less.append(city)
            if cost == pivot:
                equal.append(city)
            if cost > pivot:
                greater.append(city)
        return aweSomeSort(less, previous, sortBy) + equal + aweSomeSort(greater, previous, sortBy)  # toán tử nối mảng
    else:
        return array
