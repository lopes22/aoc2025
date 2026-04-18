file = open('day3.txt', 'r')
lines = file.readlines()

total = 0

for line in lines:
    final_line = line.strip()
    l = len(final_line)
    m = (0, 0)
    for i in range(0, l):
        n = int(final_line[i])

        if i != l - 1 and m[0] < n:
            m = (n,0)
        elif n > m[1]:
            m = (m[0], n)
    
    total += (m[0] * 10) + m[1]

print(total)