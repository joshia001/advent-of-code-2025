"""_summary_
Code that spins a dial left or right a certain number of steps. 
The dial is numbered 0 to 99. This script counts the number of times the dial
ends on a 0 after a certain instruction. 

E.g an instruction could be "L32" which means spin the dial left 32 times.

I probably could do something a lot simpler with the raw number of steps (some
sort of addition and subtraction) but I thought it would be cool to simulate
the dial as a doubly linked list.
"""

import pandas as pd

class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def insert_node_at_end(val, head):
    new_node = Node(val=val, prev=head)
    head.next = new_node
    return new_node

def create_cycle(root, tail):
    root.prev = tail
    tail.next = root

def traverse(head, val):
    visited = set()
    while head not in visited:
        visited.add(head)
        if head.val==val:
            return head
                
        head = head.next
    
def create_dial(num, cycle=True, start_pos=0):
    root = Node(val=0)
    head = Node(val=1, prev=root)
    root.next = head
    
    for i in range(2, num):
        head = insert_node_at_end(i, head)
        
    if cycle == True:
        create_cycle(root, head)
        
    start_node = traverse(root, start_pos)
    
    return start_node
    
def spin_dial(pointer, instruction, num_zeros):
    steps = int(instruction[1:])
    if instruction[0] == 'R':
        for _ in range(steps):
            pointer = pointer.next
            if pointer.val == 0:
                num_zeros += 1
            
    else:
        for _ in range(steps):
            pointer = pointer.prev
            if pointer.val == 0:
                num_zeros += 1
    return pointer, num_zeros

def main():
    num = 100
    start_pos = 50
    input_file_path = "day1\day1input.txt"
    
    pointer = create_dial(num, start_pos=start_pos)
    
    instructions = pd.read_csv(input_file_path, header=None)
    
    num_zeros = 0
    
    for instruction in instructions[0]:
        pointer, num_zeros = spin_dial(pointer, instruction, num_zeros)
    
    print("Number of times we ended on zero: ", num_zeros)

            
if __name__ == "__main__":
    main()
    
    
