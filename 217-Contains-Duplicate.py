def ContainsDuplicate(nums):
    return list(set(nums)) != list(nums)
    a = {}
    for n in nums:
        if n in a:
            return True
        a[n] = 1

    return False

print(ContainsDuplicate(range(9999999)))


