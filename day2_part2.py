import math

file = open('day2.txt', 'r')
lines = file.readlines()

ranges = []
for r in lines[0].strip().split(','):
    rr = r.split('-')
    ranges.append((int(rr[0]), int(rr[1])))

def pattern_generator(inc, start):
    if start == 0:
        return 1
    
    return pattern_generator(inc, start - inc) + 10**start 

seen = set()
total = 0
for r in ranges:
    cur_num = r[0]
    while cur_num <= r[1]:
        if cur_num < 10:
            cur_num += 1
            continue

        num_len = math.floor(math.log10(cur_num)) + 1

        first_digit = int(str(cur_num)[0])
        #see if cur_num is a single digit repeating number pattern
        if first_digit * ((10**num_len - 1) // 9) == cur_num: # ex 5 * 1111 = 5555
            if cur_num not in seen:
                seen.add(cur_num)
                total += cur_num
        else:
            stop = num_len // 2 #if this is a repeating pattern we know the pattern must repeat before the mid of the number
            cur_i = 1
            while cur_i != stop:
                num_repeating_digits = cur_i + 1
                if num_len % num_repeating_digits != 0: # we only care about possible patterns ex a 10 digit number can't have a repeating pattern of 3
                    cur_i += 1
                    continue

                #generate a number of a 1s and 0s that when cur_num is divided would equal the pattern of cur_num
                #ex: 121212 // 10101 = 12 so 121212 % 10101 = 0
                pattern = pattern_generator(num_repeating_digits, num_len - num_repeating_digits)

                if cur_num % pattern == 0:
                    if cur_num not in seen:
                        seen.add(cur_num)
                        total += cur_num             

                cur_i += 1
        cur_num += 1
    
print(total)