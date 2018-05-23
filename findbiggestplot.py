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

    best = None
    max_squares = None

    height = len(prices)
    for y in range(len(prices)):
        width = len(prices[y])

        for x in range(len(prices)):
            for i in range(height - y):
                for j in range(width - x):
                    area_width = j + 1
                    area_height = i + 1


                    price = intergal[y + i + 1][x + j + 1] + intergal[y][x] - intergal[y + i + 1][x] - intergal[y][x + j + 1]

                    if price > capital: break

                    area = area_width * area_height
                    if max_squares is not None and area < max_squares: continue
                    max_squares = area
                    best = (x, y, area_width, area_height)

    return best

print(get_biggest_plot(input, 5))