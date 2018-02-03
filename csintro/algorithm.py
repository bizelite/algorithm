def bi_search(x, nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


def reverse(s):
    if s == '':
        return s
    return reverse(s[1:]) + s[0]


def anagrams(s):
    if s == '':
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w) + 1):
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans


def rec_power(a, n):
    if n == 0:
        return 1
    else:
        factor = rec_power(a, n//2)
        if n % 2 == 0:
            return factor * factor
        else:
            return factor * factor * a


def rec_bi_search(x, nums, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    item = nums[mid]
    if item == x:
        return mid
    elif x < item:
        return rec_bi_search(x, nums, low, mid-1)
    else:
        return rec_bi_search(x, nums, mid+1, high)


if __name__ == '__main__':
    num_li = [x for x in range(10, 1800)]
    print(rec_bi_search(1500, num_li, 500, 1800))


































