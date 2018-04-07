
def quick_sort(plist):
    if len(plist) <= 1:
        return plist
    else:
        pivot = plist[0]
        less = filter(lambda x: x < pivot, plist)
        greater = filter(lambda x: x > pivot, plist)
        equal = filter(lambda x: x == pivot, plist)
        return quick_sort(less) + equal + quick_sort(greater)


def selection_sort(plist):
    sorted_list = []
    while plist:
        val = min(plist)
        sorted_list.append(val)
        plist.remove(val)
    return sorted_list


def merge_sort(plist):
    if len(plist) <= 1:
        return plist
    else:
        middle = len(plist)/2
        left = merge_sort(plist[:middle])
        right = merge_sort(plist[middle:])
        left_index = right_index = 0
        left_total = len(left)
        right_total = len(right)
        merged_list = []
        while left_index < left_total or right_index < right_total:
            if left_index == left_total:
                merged_list += right[right_index:]
                break
            if right_index == right_total:
                merged_list += left[left_index:]
                break
            if left[left_index] < right[right_index]:
                merged_list.append(left[left_index])
                left_index += 1
            else:
                merged_list.append(right[right_index])
                right_index += 1
        return merged_list
