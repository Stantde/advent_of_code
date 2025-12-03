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

...Part 2 looks nasty... not for increase in difficulty, but instead for the
larger data structure needed.
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
    evaluation_values=[None]*13
    evaluation_values[0]=int(l[0]+l[1]+l[2]+l[3]+l[4]+l[5]+l[6]+l[7]+l[8]+l[9]+l[10]+l[11])
    evaluator={}
    for z in range(12):
        evaluator[z]=l[z]
    evaluator[13]=evaluation_values
    for i in range(12,len(l)): #double check the ending number
        try:
            if evaluator[12]==l[i]:
                continue
        except KeyError:
            pass
        evaluator[12]=l[i] # Z
        evaluation_values[1]=int(evaluator[0]+evaluator[2]+evaluator[3]+evaluator[4]\
                            +evaluator[5]+evaluator[6]+evaluator[7]+evaluator[8]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[2]=int(evaluator[0]+evaluator[1]+evaluator[3]+evaluator[4]\
                            +evaluator[5]+evaluator[6]+evaluator[7]+evaluator[8]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[3]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[4]\
                            +evaluator[5]+evaluator[6]+evaluator[7]+evaluator[8]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[4]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[3]\
                            +evaluator[5]+evaluator[6]+evaluator[7]+evaluator[8]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[5]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[3]\
                            +evaluator[4]+evaluator[6]+evaluator[7]+evaluator[8]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[6]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[3]\
                            +evaluator[4]+evaluator[5]+evaluator[7]+evaluator[8]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[7]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[3]\
                            +evaluator[4]+evaluator[5]+evaluator[6]+evaluator[8]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[8]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[3]\
                            +evaluator[4]+evaluator[5]+evaluator[6]+evaluator[7]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[9]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[3]\
                            +evaluator[4]+evaluator[5]+evaluator[6]+evaluator[7]\
                            +evaluator[8]+evaluator[10]+evaluator[11]+evaluator[12])
        evaluation_values[10]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[3]\
                            +evaluator[4]+evaluator[5]+evaluator[6]+evaluator[7]\
                            +evaluator[8]+evaluator[9]+evaluator[11]+evaluator[12])
        evaluation_values[11]=int(evaluator[0]+evaluator[1]+evaluator[2]+evaluator[3]\
                            +evaluator[4]+evaluator[5]+evaluator[6]+evaluator[7]\
                            +evaluator[8]+evaluator[9]+evaluator[10]+evaluator[12])
        evaluation_values[12]=int(evaluator[1]+evaluator[2]+evaluator[3]+evaluator[4]\
                            +evaluator[5]+evaluator[6]+evaluator[7]+evaluator[8]\
                            +evaluator[9]+evaluator[10]+evaluator[11]+evaluator[12])

        evaluator[14]=max(evaluation_values)
        position = evaluation_values.index(evaluator[14])
        match position:
            case 0: # XY is max, continue on
                continue

            case 1: # 2 into 1, 3 into 2....13 into 12
                evaluation_values[0]=''
                for a in range(1,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])

            case 2: # 3 into 2, 4 into 3....13 into 12
                evaluation_values[0]=''
                for a in range(2,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            # I hope case 0, 1, 2 was enough to pick up the pattern, cuz I'm sure GOING FOR IT!
            case 3:
                evaluation_values[0]=''
                for a in range(3,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])

            case 4:
                evaluation_values[0]=''
                for a in range(4,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            case 5:
                evaluation_values[0]=''
                for a in range(5,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            case 6:
                evaluation_values[0]=''
                for a in range(6,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            case 7:
                evaluation_values[0]=''
                for a in range(7,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            case 8:
                evaluation_values[0]=''
                for a in range(8,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            case 9:
                evaluation_values[0]=''
                for a in range(9,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            case 10:
                evaluation_values[0]=''
                for a in range(10,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            case 11:
                evaluation_values[0]=''
                for a in range(11,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])
            case 12:
                evaluation_values[0]=''
                for a in range(0,13):
                    evaluator[a]=evaluator[a+1]
                for a in range(1,13):
                    evaluation_values[0]+=evaluator[a-1]
                evaluation_values[0]=int(evaluation_values[0])

            case _: # Impossible???
                print("Something went bad-wrong, my guy.")

    max_found=evaluator[14]
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
