# this function is calculating Routh-Hurwitz algorithm
def routh_hurwitz(values):
    # iterators used to iterate through rows list
    first_row_iter, second_row_iter = 0, 1
    # initialize first 2 rows with values from input
    rows = [[values[i] for i in range(len(values)) if i % 2 == 0],
            [values[i] for i in range(len(values)) if i % 2 != 0]]

    # declare rows as that row count equals to coefficients count (a0,...,an)
    if len(values) >= 2:
        for i in range(2, len(values)):
            rows.append([])

    # start criterion for all rows
    for i in range(len(rows)-2):
        first_row, second_row = rows[first_row_iter], rows[second_row_iter]
        rows[second_row_iter+1] = criterion(first_row, second_row)
        first_row_iter += 1
        second_row_iter += 1

    res = [i for i in rows if i != [0] and i != []]
    return res


# this function is calculating coefficients for new rows
def criterion(first_row, second_row):
    row = []
    if len(first_row) != len(second_row):       # add extra 0 to the row with fewer arguments (prevents errors)
        if len(first_row) > len(second_row):
            second_row.append(0)
        else:
            first_row.append(0)
    for i in range(1, len(first_row)):
        if second_row[0] == 0:
            break
        a = -(first_row[0] * second_row[i] - second_row[0] * first_row[i])/second_row[0]
        if int(a)-a == 0:       # check if 'a' can be written as integer
            row.append(int(a))
        else:
            row.append(a)
    return row


def print_results(result):
    column = []
    stable = True
    for i in result:
        print(i, len(i))
        column.append(i[0])
    for i in column:
        if abs(i) != i:
            stable = False
            break
    print(f"stable: {stable}")


if __name__ == "__main__":
    print("Write numbers from a0 to an divided by single ',' sign")
    input_array = input().split(",")
    values_array = [int(i) for i in input_array]
    results = routh_hurwitz(values_array)
    print_results(results)
