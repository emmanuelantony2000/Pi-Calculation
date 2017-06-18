x = 1
limit = 8
seriesSum = x
temp = 2

for i in range(3, limit, 2):
    y = float(1)

    for j in range(1, (i+1)):
        if j % 2 == 0:
            y /= j
        elif j % 2 == 1:
            y *= j

    y /= i
    #seriesSum += (((i-2)/(temp*i)) * (x**i))
    seriesSum += (y * (x**i))
    #temp *= 2


seriesSum *= 2
print('pi='+str(seriesSum))
