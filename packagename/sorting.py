def bubble_sort(items):
    result = items.copy()
    for x in range(len(result)):
        for y in range(len(result)-1-x):
            if result[y] > result[y+1]:
                result[y], result[y+1] = result[y+1], result[y]
    return result


def merge(a, b):
    df_merge = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            df_merge .append(a[0])
            a.pop(0)
        else:
            df_merge .append(b[0])
            b.pop(0)

    if len(a) == 0:
        df_merge  = df_merge + b
    if len(b) == 0:
        df_merge  = df_merge  + a

    return df_merge


def merge_sort(items):

    len_items= len(items)
    if len_items== 1:
        return items

    middlenum = int(len_items / 2)
    item1 = merge_sort(items[:middlenum])
    item2 = merge_sort(items[middlenum:])

    return merge(item1, item2)

def quick_sort(items, index=-1):
    len_items = len(items)

    if len_items <= 1:

        return items

    fulcrum = items[index]
    small = []
    large = []
    nul = []
    for q in items:
        if q < fulcrum:
            small.append(q)
        elif q > fulcrum:
            large.append(q)
        elif q == fulcrum:
            nul.append(q)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + nul + large


    
