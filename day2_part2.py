import math

file = open('day2.txt', 'r')
lines = file.readlines()

ranges = []
for r in lines[0].strip().split(','):
    rr = r.split('-')
    ranges.append((int(rr[0]), int(rr[1])))

def mcustom(inc, start):
    if start == 0:
        return 1
    
    return mcustom(inc, start - inc) + 10**start 

seen = set()
total = 0
for r in ranges:
    c = r[0]
    while c <= r[1]:
        if c < 10:
            c += 1
            continue

        l = math.floor(math.log10(c)) + 1

        s = str(c)
        if int(s[0]) * ((10**l - 1) // 9) == c:
            if c not in seen:
                seen.add(c)
                total += c
        else:
            stop = l // 2
            cur = 1
            while cur != stop:
                if l % (cur + 1) != 0:
                    cur += 1
                    continue

                m = mcustom(cur + 1, l - (cur + 1))

                if c % m == 0:
                    if c not in seen:
                        seen.add(c)
                        total += c             

                cur += 1
        c += 1
    
print(total)