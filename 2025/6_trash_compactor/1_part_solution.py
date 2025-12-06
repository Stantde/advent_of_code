"""
Day 6 Advent of Code 2025
Name: Demetrius Stanton
Date: 12-04-2025
"""
"""
Outline: Check each position of the paper
"""
import sys

def get_file_data(): # returns dict with key=line_number,value=line_text
    try:
        filename=(sys.argv[1])
    except IndexError:
        print(f"Please include filename in command-line.\nEx: {sys.argv[0]} \
        test.txt")
        sys.exit(2)
    foo={}    
    count =0
    with open(filename,'r') as f:
        for line in f:
            foo[count]=[fvalue for fvalue in line.strip('\n').split(' ') if fvalue !='']
            if foo[count][0] in ['+','*']:
                foo['sign']= foo[count]
                foo.pop(count, None)
            count+=1

    return foo 


def report_error(output="None added."):
    with open("error.log", 'a') as err:
        err.write(f"{output}\n")
    return


def write_result(output="Args not passed."):
    with open("result.log", 'a') as result:
        result.write(f"{output}\n")
    return
def get_sum(homework_set):
    grand_total=0    
    try:
        for pset in range(len(homework_set[0])):
            sign = homework_set['sign'][pset]
            total=0
            for key in range(len(homework_set.keys())-1):
                if total==0:
                    total=int(homework_set[key][pset])
                elif sign=='+':
                    total+=int(homework_set[key][pset])                    
                elif sign=='*':
                    total*=int(homework_set[key][pset])
            grand_total+=total
    except KeyError:
            pass
        

    
    return grand_total

def main():
    file_data=get_file_data()
    
    current_sum=get_sum(file_data)    


    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")
