from collections import defaultdict

def valid(page, rules): 
    for i, value in enumerate(page):
        if i > 0 and value in rules:            
            #print("RULE FOUND", value, rules[value])
            for j, test_value in enumerate(page[0:i]):
                #print("L", test_value)
                if test_value in rules[value]:
                    print(f"Breaks {value}|{test_value} at {i}")
                    return (False, i)
    return True

with open("input_5.txt") as fh:
    section = "rules"
    rules = defaultdict(list)
    pages = []
    for line in fh: 
        if section == 'rules' and len(line) > 1:
            r = line.strip().split('|')
            rules[r[0]].append(r[1])
        elif len(line) > 1:
            r = line.strip().split(',')
            pages.append(r)
        if line == "\n":
            section = "proposals"
            continue
    print(rules)
    print(pages)
    middles = 0 
    middles_2 = 0 
    for i, page in enumerate(pages):
        print("TESTING", page)
        result = valid(page, rules)
        if result == True:
            middles += int(page[len(page) // 2])
        else: 
            iters = 0 
            while (result != True and iters < 200):
                print("BEFORE", page, result)
                position = result[1]
                trouble_value = page[position]
                page[position] = page[position - 1]
                page[position - 1] = trouble_value
                print("AFTER", page)
                result = valid(page, rules)
                if result == True:
                    middles_2 += int(page[len(page) // 2])
                    break
                iters+=1

            
    print(">>>>TOTAL", middles)
    print(">>>>TOTAL 2", middles_2)