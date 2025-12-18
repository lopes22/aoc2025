file = open('day2.txt', 'r')
lines = file.readlines()

ranges = []
for r in lines[0].strip().split(','):
    rr = r.split('-')
    ranges.append((int(rr[0]), int(rr[1])))

total = 0
for r in ranges:
    c = r[0]
    while c <= r[1]:
        if c < 10:
            c += 1
            continue
        
        s = str(c)

        if len(s) % 2 == 0:
            m = len(s) // 2
            f = int(s[:m])
            l = int(s[m:])

            if l == 0:
                c += 1
                continue

            if f / l == 1:
                total += c

        c += 1
    
print(total)