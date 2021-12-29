# time: 0(n) | space: 0(n)
def twoNumberSum(array, targetSum):
    # intialize an empty dictionary of key value pairs
    nums = {}
    """create a for loop that goes through the array and:
    1. sets a potentialMatch by subtracting i from the targetSum
    2. if the potentialMatch is in the dictionary return it
    3. otherwise return the dictionary value at index i
    """
    for i in array:
        potentialMatch = targetSum - i
        if potentialMatch in nums:
            return [potentialMatch, i]
        else:
            nums[i] = True
    return []

print(twoNumberSum({3, 5, -4, 8, 11, 1, -1, 6}, 10))