"""return first 2 indexes (in list) from the list whose sum is equal to the given number"""
def sum_indexes(numbers: list, target: int) -> list:
    seen = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        if number not in seen:  # To avoid using the same element twice
            seen[number] = index
    return []

if __name__ == "__main__":
    nums = [10, 20, 10, 40, 50, 60, 70]
    target_value = 50
    result = sum_indexes(nums, target_value)
    print(f"Indexes of numbers that sum to {target_value}: {result}")
              