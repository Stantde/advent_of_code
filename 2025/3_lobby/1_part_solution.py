"""
Day 3 Advent of Code 2025
Name: Demetrius Stanton
Date: 12-03-2025
"""
"""
Outline: Create an 'evaluator' data struct to quickly compare the next entry.
Evaluator starts at index 0, assigns the value there into key = 0. It moves on
to index 1, and assigns the value there into key 1. Value at key 0 and value
at key 1 are concatenated, converted to int, and stored in list in key 3 index
0.

Now the magic happens, iterate to index 2 (n+1), and store the value in key=2.
Value at key 1 and value at key 2 are concatenated, converted to int, and
stored in index 1 of list in key 3. Value at key 0 and value at key 2 are
concatenated, converted to int, and stored in index 2 of list in key 3.

key 4 holds max of list in key 3, indicating the shifts to occur to get that
outcome. At end of iteration, return max for final summation.
"""
import sys

def get_file_data(): # returns dict with key=line_number,value=line_text
    try:
        filename=(sys.argv[1])
    except IndexError:
        print(f"Please include filename in command-line.\nEx: {sys.argv[0]} \
        test.txt")
        sys.exit(2)
    file_output={}
    count=0
    with open(filename,'r') as f:
        for line in f:
            file_output[count]=line.strip('\n')
            count+=1
    return file_output

def evaluate(l):
    max_found=None
    evaluation_values=[None]*3
    evaluation_values[0]=int(l[0]+l[1])
    evaluator={0:l[0], # X
               1:l[1], # Y
               3:evaluation_values} #[xy, xz, yz]
    for i in range(2,len(l)): #double check the ending number
        try:
            if evaluator[2]==l[i]:
                continue
        except KeyError:
            pass
        evaluator[2]=l[i] # Z
        evaluator[3][1]=int(evaluator[0]+evaluator[2])
        evaluator[3][2]=int(evaluator[1]+evaluator[2])
        evaluator[4]=max(evaluation_values)
        position = evaluator[3].index(evaluator[4])
        match position:
            case 0: # XY is max, continue on
                continue

            case 1: # XZ is max, move Z into Y, update evaluation_values[0]
                evaluator[1]=evaluator[2]
                evaluation_values[0]=int(evaluator[0]+evaluator[1])

            case 2: # YZ is max, move Y into X, move Z into Y, update evaluation_values[0]
                evaluator[0]=evaluator[1]
                evaluator[1]=evaluator[2]
                evaluation_values[0]=int(evaluator[0]+evaluator[1])

            case _: # Impossible???
                print("Something went bad-wrong, my guy.")

    max_found=evaluator[4]
    write_result(f"Given: {l},\nFound max: {str(max)}")
    return max_found

def report_error(output="None added."):
    with open("error.log", 'a') as err:
        err.write(f"{output}\n")
    return


def write_result(output="Args not passed."):
    with open("result.log", 'a') as result:
        result.write(f"{output}\n")
    return

def main():
    file_data=get_file_data()
    max_list=[]
    current_sum=0
    for line in file_data.values():
        max_list.append(evaluate(line))
    current_sum=sum(max_list)

    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")
