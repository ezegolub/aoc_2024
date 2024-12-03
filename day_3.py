import re
pattern = re.compile(r"(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)")
total = 0
enabled = True
with open("input_3.txt") as fh:
    for line in fh:
        matches = pattern.findall(line)
        for m in matches:
            print(m)
            if m[0] == "do()":
                
                print("Enabling")
                enabled = True
            elif m[1] == "don't()":
                print("Disabling")
                enabled = False
            elif enabled:
                total += int(m[2]) * int(m[3])
                print("summing", total)
print(total)

# 92349994 -- TOO LOW
# 93275066 -- TOO LOW