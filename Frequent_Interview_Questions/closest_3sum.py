
def closestSum(arr,k):

    # initialising the closest to the highest value
    closest = float("inf")

    # sorting the array so that we can use two pointer method
    arr.sort()

    for i in range(len(arr) - 2):
        # Initialising the two pointers
        left = i + 1
        right = len(arr) - 1

        while left < right:
            # taking the sum
            sum3 = arr[i] + arr[left] + arr[right]

            # if the absolute value of difference between  the sum and target is less than the absoulte value of differennce
            # between the  closest and target , then closest = sum
            if abs(k - sum3) < abs(k - closest):
                closest = sum3

            # decreasing the right pointer
            elif sum3 > k:
                right -= 1

            # Increasing the left pointer
            else:
                left += 1
    return closest



arr = [-1,2,-1,4]
print(closestSum(arr, 1))