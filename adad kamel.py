import timeit

def adad_kamel(n):
    sum = 1
    i = 2
    x = n ** 0.5
    while (i <= x):
        if (n % i == 0):
            sum += i
            if (i != (n / i)):
                sum += n / i
        i += 1

    if (sum == n):
        return True
    return False
n = int(input("inter num:"))
start = timeit.default_timer()
for j in range(n):
    if (adad_kamel(j)):
        print(j)
stop = timeit.default_timer()

print('Time:', stop - start)