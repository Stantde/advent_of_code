"""
Day 7 Advent of Code 2025
Name: Demetrius Stanton
Date: 12-07-2025
"""
"""

"""
import sys

def get_file_data(): # returns dict with key=line_number,value=line_text
    try:
        filename=(sys.argv[1])
    except IndexError:
        print(f"Please include filename in command-line.\nEx: {sys.argv[0]} \
        test.txt")
        sys.exit(2)
    lines=[]
    with open(filename,'r') as f:
        for line in f:
            lines.append(line.strip('\n'))
    return lines

def report_error(output="None added."):
    with open("error.log", 'a') as err:
        err.write(f"{output}\n")
    return


def write_result(output="Args not passed."):
    with open("result.log", 'a') as result:
        result.write(f"{output}\n")
    return

def main():
    tachyon_field=get_file_data()
    beam='|'
    for step in tachyon_field:
        if 'S' in step:
            starting_position=step.index('S')
            current_position=starting_position
            next_position=current_position
            print(f"{step.replace('S',beam)}")
            continue
        if step[next_position]=='.':
            step.replace=beam
        elif step[next_position]=='^':
            ...
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
