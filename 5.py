for i in range (len(x)):
    for j in range (len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
for i in result:
    print(r)