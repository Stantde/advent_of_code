"""
Day 2 Advent of Code 2025
Name: Demetrius Stanton
Date: 12-02-2025
"""
"""
Outline: Based on command-line args, operate on list of nums, incrementing 
counter each time the 'zero-th' position is the result of the operation.

Expected outcome from test.txt is 3.
"""
import sys

def get_file_data():
    # Get command line args.
    try:
        filename=(sys.argv[1])
    except IndexError:
        print(f"Please include filename in command-line.\nEx: {sys.argv[0]} \
        test.txt")
        sys.exit(2)
    with open(filename,'r') as f:
        return f
    
def separate_IDs_by_commas(ID_ranges):
     ID=[]
     ID = ID_ranges.split(',')
     return ID

def validate_IDs(ID):
     
     return

def main():
    file_data=get_file_data()
    ID=separate_IDs_by_commas(file_data)
    file_data.close()
    invalid_IDs=[]
    for ID_range in ID:
        invalid_IDs.append(validate_IDs(ID_range)) #These refer to the same array, yes?
        #will invalid ids require further processing before summation?
    return



if __name__=='__main__':
    print(f"The password is: {main()}.")