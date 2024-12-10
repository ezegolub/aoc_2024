import re
pattern = re.compile(r"(XMAS)|(SAMX)")
total = 0 
enabled = True
lines = []

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0].strip()))]

def diagonal_hits(matrix):
    total = 0 
    i = 0
    while i < len(matrix) * 2  - 1:
        if (i > len(matrix) - 1): 
            pos_x = i - len(matrix) + 1
            pos_y = len(matrix) - 1
        else: 
            pos_x = 0
            pos_y = i 
        line = ""
        while pos_y >= 0 and pos_x < len(matrix[0]):  
            line += matrix[pos_y][pos_x]
            pos_x += 1
            pos_y += -1
        total += len(pattern.findall("".join(line)))
        
        i+=1
    return total



def inverse_diagonal_hits(matrix):
    total = 0 
    i = 0
    while i < len(matrix) * 2  - 1:
        if (i > len(matrix) - 1): 
            pos_x = i - len(matrix) + 1
            pos_y = 0
        else: 
            pos_x = 0
            pos_y = len(matrix) - 1 - i
        line = ""
        while pos_x >= 0 and pos_y < len(matrix) and pos_x < len(matrix): 
            line += matrix[pos_y][pos_x]
            pos_x += 1
            pos_y += 1
        total += len(pattern.findall("".join(line)))
        i+=1
    return total

with open("input_4.txt") as fh:
    for line in fh:
        lines.append(line)

for line in lines:
    total += len(pattern.findall(line))
print("HORIZONTAL", total)
for line in transpose(lines):
    total += len(pattern.findall("".join(line)))
print("VERTICAL", total)
total+=diagonal_hits(lines)
print("DIAG 1", total)
total+=inverse_diagonal_hits(lines)
print("DIAG 2", total)
print("----TOTAL", total)

# 443 horizontal
# 1626 hor + vert + diag 
# 2409 -- too low 