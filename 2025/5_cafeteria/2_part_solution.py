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
    fresh_ingredient_id_ranges={}
    available_ingredient_ids={}
    switch=False
    count=0
    with open(filename,'r') as f:
        for line in f:
            if switch:
                if line:
                    available_ingredient_ids[line.strip('\n')]='u'
                    continue
            if line == '\n':
                switch= True
                continue
            fresh_ingredient_id_ranges[count]=line.strip('\n')
            count+=1

    return fresh_ingredient_id_ranges,available_ingredient_ids

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
    id_ranges,ids=get_file_data()
    current_sum=0
    for key in id_ranges.keys():
        lower=id_ranges[key].split('-')[0]
        upper=id_ranges[key].split('-')[1]
        new_ranges=[]
        new_ranges.append(int(lower))
        new_ranges.append(int(upper))
        id_ranges[key]=new_ranges
    for ingredient in ids.keys():
        for key in id_ranges.keys():
            if (int(ingredient)>=id_ranges[key][0] ) and (int(ingredient)<=id_ranges[key][1] ):
                if ids[ingredient]=='u':
                    current_sum+=1
                ids[ingredient]='f'
                print(f"{ingredient} is fresh, in {key}.")


    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")
