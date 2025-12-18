file = open('day1.txt', 'r')
lines = file.readlines()

c = 50
zero = 0
for l in lines:
    d = l[0]
    n = int(l[1:])

    if d == 'R':
        t = c + n
        zero += t // 100
        c = t % 100
    else:
        t = c - n
        if t <= 0:
            if c != 0:
                zero += 1

            zero += t // -100

        c = t % 100
    
print(zero)