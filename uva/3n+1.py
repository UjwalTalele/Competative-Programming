def get_length(num):
    cycle = []
    k = num
    cycle.append(num)
    while(k != 1):
        if(k % 2 == 0):
            k = k/2
        else:
            k = 3*k+1
        cycle.append(k)
    return(len(cycle))


n = 1
while(n > 0):
    ab = list(map(int, input().split()))
    a = ab[0]
    b = ab[1]
    lengths = []
    for item in range(a, b+1):
        lengths.append(get_length(item))
    n += 1
    print('{} {} {}'.format(a, b, max(lengths)))
    if (EOFError):
        break
