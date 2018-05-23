input = [
    [1, 4, 6, 7],
    [2, 5, 3, 1],
    [1, 1, 1, 1],
    [9, 1, 0, 1]
]

test_intergal = [
    [1, 5, 11, 18],
    [3, 12, 21]
]

def get_intergal(prices):
    result = [[0 for i in range(len(prices[0]) + 1)]]

    for y in range(len(prices)):
        row = [0]
        result.append(row)
        for x in range(len(prices[y])):
            total = prices[y][x]

            total += result[y + 1][x]

            total += result[y][x + 1]

            total -= result[y][x]

            row.append(total)

    return result


def get_biggest_plot(prices, capital):
    intergal = get_intergal(prices)
    iterations = 0

    best = None
    max_squares = None

    height = len(prices)
    for y in range(len(prices)):
        width = len(prices[y])

        for x in range(len(prices)):
            for i in range(height - y):
                min_valid = 0
                max_valid = width - x

                j = None
                next = (width - x) // 2

                while j != next:
                    j = next
                    iterations += 1

                    area_width = j + 1
                    area_height = i + 1

                    print(x,y,j,i)
                    price = intergal[y + i + 1][x + j + 1] + intergal[y][x] - intergal[y + i + 1][x] - intergal[y][x + j + 1]

                    if price <= capital:
                        area = area_width * area_height
                        if max_squares is None or area > max_squares:
                            max_squares = area
                            best = (x, y, area_width, area_height)
                        
                        next = (j + max_valid) // 2
                        min_valid = next

                    else:
                        next = (j + min_valid) // 2
                        max_valid = next


    return (best, iterations)

# ((1, 2, 3, 2), 63)
print(get_biggest_plot(input, 5))