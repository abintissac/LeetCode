def mean(data):
    return sum(data) / len(data)

def pearson(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    sum_of_diff = 0

    for i in range(n):
        sum_of_diff += (x[i] - mean_x) * (y[i] - mean_y)

    sum_sqx = 0
    for i in range(n):
        sum_sqx += (x[i] - mean_x) ** 2

    sum_sqy = 0
    for i in range(n):
        sum_sqy += (y[i] - mean_y) ** 2

    coeff = sum_of_diff / ((sum_sqx * sum_sqy) ** 0.5)
    return coeff

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
corr_coefficient = pearson(x, y)

# Output the result
print("Pearson correlation coefficient:", corr_coefficient)
