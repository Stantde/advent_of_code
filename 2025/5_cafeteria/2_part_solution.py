"""
Day 4 Advent of Code 2025
Name: Demetrius Stanton
Date: 12-05-2025
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
                break
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
    current_ranges = []
    for main_key in range(len(id_ranges.keys())):
        add_me=True
        correction=0
        c=id_ranges[main_key][0]
        d=id_ranges[main_key][1]
        if current_ranges:#cd
            for r in current_ranges:#ab
                a=r[0]
                b=r[1]
                if (a<c<b)and(a<d<b): #ab includes cd
                    add_me=False
                    break
                elif (c<a<d)and(c<b<d):#a-b bw cd
                    correction= -1*(b-a+1)
                elif (c<a<d and d<b):# a only bw cd
                    if a-1<0:
                        raise UnexpectedExpectedError
                    id_ranges[main_key][1]=a-1
                    d=id_ranges[main_key][1]
                elif (c<b<d and a<c):# b bwt cd
                    id_ranges[main_key][0]=b+1
                    c=id_ranges[main_key][0]
                else:
                    ...
            if add_me:
                current_sum+=id_ranges[main_key][1]-id_ranges[main_key][0] +1 + correction
                current_ranges.append(id_ranges[main_key])

        else:
            current_ranges.append(id_ranges[main_key])
            current_sum+=id_ranges[main_key][1]-id_ranges[main_key][0] +1


    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")
