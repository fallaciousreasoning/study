def naive_pair_that_sum(numbers, sum):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i == j: continue

            if numbers[i] + numbers[j] == sum:
                return True

    return False

def bs_pair_that_sum(numbers, sum):
    sorted_numbers = sorted(numbers)

    for i in range(len(sorted_numbers)):
        current = sorted_numbers[i]
        left = i + 1
        right = len(sorted_numbers)

        while True:
            guess_index = (left + right) // 2
            if left == right: break

            result = current + sorted_numbers[guess_index]
            if result == sum:
                return True

            if result < sum:
                left = guess_index + 1

            if result > sum:
                right = guess_index - 1

    return False

def hash_pair_that_sum(numbers, sum):
    s = {}
    for number in numbers:
        if not number in s:
            s[number] = 0

        s[number] += 1

    for number in numbers:
        complement = sum - number
        if complement in s and (complement != number or s[number] != 1):
            return True

    return False

def linear_pair_that_sum(numbers, sum):
    i = 0
    j = len(numbers) - 1

    while i < j:
        current = numbers[i] + numbers[j]

        if current == sum: return True
        if current < sum: i += 1
        if current > sum: j -= 1

    return False

def better_hash_pair_that_sum(numbers, sum):
    seen = set()

    for number in numbers:
        complement = sum - number

        if complement in seen:
            return True

        seen.add(number)

    return False

print(better_hash_pair_that_sum([1,2,3,4], 8))
print(better_hash_pair_that_sum([1,2,3,4,4], 8))
