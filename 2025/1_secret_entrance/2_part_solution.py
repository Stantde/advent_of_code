"""
Day 1 Advent of Code 2025
Name: Demetrius Stanton
Date: 12-01-2025
"""
"""
Outline: Based on command-line args, operate on list of nums, incrementing 
counter each time the 'zero-th' position is clicked. 

Expected outcome from test.txt is 3.
"""
import sys
BEGINNING_STATE=50
RECURSIONLIMIT=10000
sys.setrecursionlimit(RECURSIONLIMIT) # 1000 isn't enough? Neither is 10000? That CAN'T be right...


def decode(instruction): 
    """ 
    Takes instruction of the form 'Dnnne', where D represents the direction of 
    rotation ([L]eft or [R]ight), nnn represents a 1 to 3 digit number of 
    shifts to take in the given direction, and e represents the end character,
    typically '\n', but possibly 'EOF'.

    Returns a tuple of two numbers, (x,y). x can be positive or negative with a 
    range of -999 to +999. y is one of two numbers, 0 or 1. 
    """
    x=None
    y=None
    try:
        x=int(instruction[1:len(instruction)-1])
    except ValueError:
        print("manually assigning x = 100")
        x=0
    if instruction[0] =='L':
        x*=-1        
    if ord(instruction[len(instruction)-1]) == 50:
        y=0
    else:
        y=1
    return (x,y)
def generate_safe(): 
    """
    Creates a range of numbers, 0 to 99 which represent the different positions
    on a safe. Returns a list whose value at an index is equal to it's index.
    """
    n=[]
    for value in range(100):
        n.append(value)
    return n
def manage_state(current, next, zeros):
    """
    Exactly what cases are possible?
    Current 0-99.
    next -999-+999
    ok...
    current 
    c>0, c=0 
    n--, n-, n0, n+, n++

    Normalize n to +/- 100
    """

    while (next<-99):
        next+=100
        zeros+=1
    while (next>99):
        next-=100
        zeros+=1
    
    # next is never 0 or 100.
    new_position = next + current
    if (next<0):
        if (new_position<0):
            new_position+=100
            if (current==0):
                return new_position, zeros
            zeros+=1
    if (new_position>99):
        new_position-=100
        zeros+=1
    elif (new_position==0):
        zeros+=1
    
    return new_position, zeros
# 7375???

def main():
    # Get command line args.
    try:
        filename=(sys.argv[1])
    except IndexError:
        print(f"Please include filename in command-line.\nEx: {sys.argv[0]} \
        test.txt")
        sys.exit(2)
    with open(filename,'r') as f:
        current=BEGINNING_STATE
        safe=generate_safe() # Nice idea, but is it really necessary?        
        zeros=0
        line_count=1
        for line in f:
            next=decode(line) # Yields a tuple with direction and whether or not to continue, not that the latter matters. 
            print(f"{current} input: {line}")
            if line_count==139:
                ...
            current,zeros=manage_state(current, next[0], zeros)# how do I retieve the safe's state?
            print(f"result: {current}, interpreted move: {next[0]} count of zeros: {zeros}")            
            print(f"line count: {line_count}")
            line_count+=1
    return zeros

if __name__=='__main__':
    print(f"The password is: {main()}.")