file = open('day1.txt', 'r')
lines = file.readlines()

c = 50
zero = 0
for l in lines:
    d = l[0]
    n = int(l[1:])

    if d == 'R':
        c = (c + n) % 100
    else:
        c = (c - n) % 100

    if c == 0:
        zero += 1
    
print(zero)