"""
Day 4 Advent of Code 2025
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
    file_output=[]
    with open(filename,'r') as f:
        for line in f:
            file_output.append(line.strip('\n'))

    return file_output

def evaluate(l):
    count=0
    row_length=len(l)
    col_length=len(l[0])
    roll='@'
    for r in range(row_length):
        for c in range(col_length):
            if l[r][c] == roll:
                l[r][c].replace(roll,'x')
                count+=1



    write_result(f"Given: {l},\nFound max: {str(count)}")
    return count

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
    row_length=len(file_data)
    col_length=len(file_data[0])
    for line in range(row_length):
        file_data[line]=list(file_data[line])
    roll='@'
    for r in range(row_length):
        for c in range(col_length):
            if file_data[r][c] == roll:
                # Count number of adjacent rolls
                count=0
                for a in range(-1,2):
                    for b in range(-1,2):
                        if a==0 and b==0:
                            continue
                        if a+r < 0 or a+r>row_length-1:
                            continue
                        if b+c < 0 or b+c>col_length-1:
                            continue
                        if file_data[a+r][b+c] in [roll,'x']:
                            count+=1
                if count<4:
                    file_data[r][c]='x'
                    current_sum+=1

    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")
