def print_info(a):
    n = len(a)
    avg = 0.0
    for i in range(n):
        print("Element #%d is %d" % (i,a[i]))
        avg += a[i]
    avg /= n
    print("Average is %f" % avg)