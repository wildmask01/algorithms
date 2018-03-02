

def search1(plist, needle):
    """
    :param plist:
    :param needle:
    :return:
    """
    if not plist:
        return -1
    middle = len(plist)/2
    if needle == plist[middle]:
        return middle
    return search(plist[0:middle], needle) if plist[middle] > needle else middle + search(plist[middle:], needle)


def search2(plist, needle):
    low = 0
    high = len(plist) - 1

    while low <= high:
        middle = (low + high) / 2
        if plist[middle] == needle:
            return middle
        else:
            if needle < plist[middle]:
                high = middle - 1
            else:
                low = middle + 1
    return None

def search(plist, needle):
    search2(plist, needle)

if __name__ == '__main__':
    print search([1, 2, 3, 6, 8, 9], 8)
