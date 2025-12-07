"""
Day 4 Advent of Code 2025
Name: Demetrius Stanton
Date: 12-05-2025
"""
"""
Outline: The initial plan did not work. So I will now attempt to implement 
an interval merging algorithm, then proceed to calculate the count of the IDs 
in a given interval.
"""
import sys

def get_file_data(): # returns dict with key=line_number,value=line_text
    try:
        filename=(sys.argv[1])
    except IndexError:
        print(f"Please include filename in command-line.\nEx: {sys.argv[0]} \
        test.txt")
        sys.exit(2)
    fresh_ingredient_id_ranges=[]
    with open(filename,'r') as f:
        for line in f:
            if line == '\n':
                break
            fresh_ingredient_id_ranges.append(line.strip('\n'))
    return fresh_ingredient_id_ranges

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0]) 
    merged = []
    current_start, current_end = intervals[0]
    for next_start, next_end in intervals[1:]:
        if current_end >= next_start:
            current_end = max(current_end, next_end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = next_start, next_end
    merged.append([current_start, current_end])
    return merged

def report_error(output="None added."):
    with open("error.log", 'a') as err:
        err.write(f"{output}\n")
    return


def write_result(output="Args not passed."):
    with open("result.log", 'a') as result:
        result.write(f"{output}\n")
    return

def main():
    raw_id_ranges=get_file_data()
    parsed_ranges=[]
    for line in raw_id_ranges:
        try:
            lower, upper = map(int, line.split('-'))
            parsed_ranges.append([lower, upper])
        except ValueError:
            continue
    merged_ranges = merge_intervals(parsed_ranges)
    current_sum = 0
    for start, end in merged_ranges:
        current_sum += (end - start + 1)
    return str(current_sum)        
    

if __name__=='__main__':
    print(f"The sum is: {main()}.")

# 432577839375365 Too high.
# 363576316169882 That's not right.
# 342433357244012 <help from someone online
