def Search2DMatrix(mtr, target):
    if mtr[0][0] > target:
        return False
    def hello(target, start=0, end=len(mtr) -1):
        mid = round((start + end) / 2)
        if (mtr[mid][-1]) >= target and mtr[mid][0] <= target:
                return mtr[mid]
        if start > end or start == end:
            return False
        if target >= (mtr[mid][-1]):
            return hello(target, start=mid + 1, end=end)
        elif target <= (mtr[mid][-1]):
            return hello(target, start=start, end=mid - 1)
    
    row = hello(target)
    if row != False:
        def checkTarget(target, start=0, end=len(row) - 1):
            middle = round((start + end) / 2)
            if row[middle] == target:
                return True
            if start == end:
                return False
            if row[middle] <= target:
                return checkTarget(target, start=middle + 1, end=end)
            if row[middle] >= target:
                return checkTarget(target, start, end=middle - 1)
        return checkTarget(target)

    return False
print(
Search2DMatrix([[1,3,5,7,8],[9,12,15,19,21],[22,24,27,29,30],[32,34,36,37,38],[40,42,46,47,48]],38)
)