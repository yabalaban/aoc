import utils 

inp = utils.download_input(day=7)
rows = [row.strip() for row in inp]


def validate(goal, nums, acc, concat=False):
    if not nums:
        return goal == acc
    val = nums[0]
    return validate(goal, nums[1:], acc + val) or validate(goal, nums[1:], acc * val) or validate(goal, nums[1:], int(str(acc) + str(val)))


res = 0
for row in rows: 
    items = row.split(":")
    goal = int(items[0])
    nums = [int(n) for n in items[1].split()]
    if validate(goal, nums[1:], nums[0]):
        res += goal
print(res)