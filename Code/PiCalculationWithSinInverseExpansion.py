x = 1
limit = 22222
seriesSum = x

for i in range(3, limit, 2):
    y = float(1)

    for j in range(1, i):
        if j % 2 == 0:
            y /= j
        else:
            y *= j

    y /= i
    seriesSum += (y * (x**i))


seriesSum *= 2
print('pi='+str(seriesSum))
