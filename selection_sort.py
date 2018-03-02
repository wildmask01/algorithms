
def find_smallest(plist):
    return min(plist)


def sort(plist):
    sorted_list = []
    while plist:
        val = find_smallest(plist)
        sorted_list.append(val)
        plist.remove(val)
    return sorted_list

if __name__ == '__main__':
    print sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
