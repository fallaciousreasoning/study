name = 'minscalarproduct'

def load_test_cases(data_set):
    filename = f'{name}.{data_set}.in'

    with open(filename) as f:
        n = int(f.readline())

        for i in range(n):
            f.readline()

            x = [int(i) for i in f.readline().split(' ')]
            y = [int(i) for i in f.readline().split(' ')]

            yield (x, y)

def dot(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * y[i]

    return sum

def permutations(x):
    if len(x) == 1:
        yield x
        return

    for i in range(len(x)):
        without = x[:]
        item = without.pop(i)

        permutations_without = permutations(without)
        for permuation in permutations_without:
            yield [item] + permuation

def naive_min_dot(x, y):
    min_so_far = None

    for v1 in permutations(x):
        for v2 in permutations(y):
            d = dot(v1, v2)
            if min_so_far is None or d < min_so_far:
                min_so_far = d

    return min_so_far

def min_dot(x, y):
    # Multiply biggest negatives by biggest positives
    sorted_x = sorted(x)
    sorted_y = sorted(y, reverse=True)

    return dot(sorted_x, sorted_y)

def run_on(data_set='small'):
    with open(f'{name}.{data_set}.out', 'w') as f:
        i = 1
        for x, y in load_test_cases(data_set):
            value = min_dot(x, y)
            f.write(f'Case #{i}: {value}\n')
            i += 1

run_on('small')
run_on('large')
    