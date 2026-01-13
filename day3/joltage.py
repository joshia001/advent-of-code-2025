import pandas as pd
from collections import deque

# I used a deque because for the first half of the day 3 puzzle I utilised the
# popleft() function. Although I removed this in my final solution, I left the
# code skeleton largely untouched.

# The workflow for this script was drafted for the 2-battery case and the logic
# extended for the 12-battery case:
# 1. Start with the first n batteries
# 2. If there is a larger battery in front of a smaller battery
#    e.g the 5 in '453':
#    2a. pop the smaller battery
#    2b. shift all the batteries up
#    2c. append the next battery in the bank

def main():
    # Prep input data (series of banks)
    input_file_path = 'day3\day3input.txt'
    banks = pd.read_csv(input_file_path, header=None)
    
    # How many batteries should be turned on per bank
    max_num_on = 12
    
    tot_joltage = 0
    
    for bank in banks[0]:
        joltage = ''
        on_batteries = deque([])
        
        bank = str(bank)
        for battery in bank:
            
            if len(on_batteries) < max_num_on:
                on_batteries.append(battery)
                continue
            
            for i in range(len(on_batteries)-1):
                if on_batteries[i+1] > on_batteries[i]: # 2.
                    del on_batteries[i] # 2a. & 2b.
                    on_batteries.append(battery) # 2c.
                    break
            
            if battery > on_batteries[-1]:
                on_batteries.pop()
                on_batteries.append(battery)
                
        for i in range(max_num_on):
            joltage += on_batteries[i]

        tot_joltage += int(joltage) 
            
    print(f'Total output joltage: {tot_joltage}')
    
if __name__ == '__main__': 
    main()