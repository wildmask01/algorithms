

def recursive_sum_1(plist):
    if not plist:
        return 0
    else:
        return plist[0] + recursive_sum(plist[1:])


def recursive_sum_2(plist):
    return reduce(lambda x, y: x+y, plist, 0)
