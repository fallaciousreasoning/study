name = 'milkshakes'

def any_unsatisfied(customers, flavors):
    for like in customers:
        satisfied = [pref for pref in like if flavors[pref[0] - 1] == pref[1]]
        if len(satisfied) == 0: return True

    return False

def satisfy(num_flavors, customer_preferences):
    make = {}
    n_customers = len(customer_preferences)

    for flavor in range(num_flavors): make[flavor] = 0

    for i in range(len(customer_preferences)):
        prefs = customer_preferences[i]
        if len(prefs) != 1 or prefs[0][1] == 0:
            continue

        make[prefs[0][0] - 1] = 1
        if any_unsatisfied(customer_preferences[:i], make):
            return "IMPOSSIBLE"        

    return ' '.join([str(make[i]) or 0 for i in range(num_flavors)])

def test(size='small'):
    infile = f'{name}.{size}.in'
    outfile = f'{name}.{size}.out'

    tests = []

    with open(infile) as f:
        num_tests = int(f.readline())

        for i in range(num_tests):
            num_flavors = int(f.readline())
            num_customers = int(f.readline())
            customers = []

            for j in range(num_customers):
                numbers = f.readline().split(' ')
                num_prefs = int(numbers[0])
                prefs = []

                for i in range(1, num_prefs*2 + 1, 2):
                    prefs.append((int(numbers[i]), int(numbers[i + 1])))

                customers.append(prefs)
            
            tests.append((num_flavors, customers))

    with open(outfile, 'w') as f:
        for index, t in enumerate(tests):
            result = satisfy(*t)
            f.write(f'Case #{index + 1}: {result}\n')


# test('small')
#test('large')

# print(satisfy(5, [[(1, 1)], [(1, 0), (2, 0)], [(5, 1), (4, 0)]]))
print(satisfy(2, [[(1,1)], [(1, 0), (2, 1)]]))
# TODO: How to deal with malted if its not the only item?