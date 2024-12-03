def is_safe(report):
    decreasing = report[0] < report[1]
    for v, _ in enumerate(report[:-1]):
        dif = abs(report[v] - report[v+1])
        if dif < 1 or dif > 3:
            return False
        if decreasing: 
            if report[v] >= report[v+1]:
                return False
        else:
            if report[v] <= report[v+1]:
                return False
    return True

total = 0
with open("input_2.txt") as f:
    for line in f:
        report = list(map(int, line.strip().split(" ")))
        if is_safe(report):
            #print(report, "safe")
            total += 1
        else: 
            print(report, "not safe")
            safe = False
            for i in range(len(report)):
                r2 = report[:]
                del r2[i]
                print(report, f"removing {i}", r2)
                if is_safe(r2):
                    print(r2, f"safe after removing {i}")
                    total+=1
                    safe = True
                    break
            if not safe: 
                print("not safe after permutations")
                
print(total)
        