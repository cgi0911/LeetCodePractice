import random

def partition(nums, st, ed):
    if st >= ed:
        return

    pivot = nums[ed]
    p1 = st - 1

    for p2 in range(st, ed):
        # p2 = st, st+1, ..., ed-1
        if nums[p2] < pivot:
            p1 += 1
            nums[p1], nums[p2] = nums[p2], nums[p1]

    nums[p1+1], nums[ed] = nums[ed], nums[p1+1]

    partition(nums, st, p1)
    partition(nums, p1+1, ed)


def quickSort(nums):
    if len(nums) <= 1:
        return

    partition(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    n = int( input("# of integers: ") )
    nums = random.sample(range(n), n)

    print ("Original list:")
    print (nums)

    quickSort(nums)

    print ("Sorted list:")
    print (nums)
