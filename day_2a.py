total = 0
with open("input_2.txt") as f:
    for line in f:
        report = list(map(int, line.strip().split(" ")))
        safe = True
        decreasing = report[0] < report[1]
        for v, i in enumerate(report[:-1]):
            dif = abs(report[v] - report[v+1])
            if dif < 1 or dif > 3:
                safe = False
                break
            if decreasing: 
                if report[v] >= report[v+1]:
                    safe = False
                    break
            else:
                if report[v] <= report[v+1]:
                    safe = False
                    break
        if safe:
            total += 1
print(total)
        