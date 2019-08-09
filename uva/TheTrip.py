fin = []
while(True):
    n = int(input())
    if(n > 0):
        amt = []
        for i in range(n):
            amt.append(float(input()))
        avg = float(sum(amt)/n)
        new = [x for x in amt if x < avg]
        total = 0
        for num in new:
            total = float(total) + abs(avg-num)
        fin.append(format(round(total, 2), '.2f'))
    else:
        break
for x in fin:
    print("${}".format(x))
