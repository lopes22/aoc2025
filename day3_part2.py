file = open('day3.txt', 'r')
lines = file.readlines()

total_joltage = 0
batteries_needed = 12

for line in lines:
    bank = line.strip()
    bank_len = len(bank)
    batteries_on = [0] * batteries_needed

    for i in range(bank_len):
        cur_battery = int(bank[i])

        available_slots = min(bank_len - i, batteries_needed)

        for pos in range(batteries_needed - available_slots, batteries_needed):
            if cur_battery > batteries_on[pos]:
                batteries_on[pos] = cur_battery
                batteries_on[pos + 1:] = [0] * len(batteries_on[pos + 1:])
                
                break
    
    for k in range(batteries_needed):
        total_joltage += batteries_on[k] * (10 **(batteries_needed - k - 1))

print(total_joltage)