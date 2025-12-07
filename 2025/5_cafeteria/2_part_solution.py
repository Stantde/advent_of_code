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
    fresh_ingredient_id_ranges={}
    count=0
    with open(filename,'r') as f:
        for line in f:
            if line == '\n':
                break
            fresh_ingredient_id_ranges[count]=line.strip('\n')
            count+=1
    return fresh_ingredient_id_ranges

def merge_intervals(r):
    """
    Docstring for merge_intervals
    
    :param r: Description r is is a dict containing id ranges which may or may
    not have overlapping ranges. The first task is to determine if the ranges 
    overlap. If two ranges overlap, merge them into a single range, updating 
    the initial range, and removing the second.

    # Using a default value to prevent KeyError
    removed_value_safe = my_dict.pop('grape', None) # 'grape' does not exist
    print(f"Removed value (safe): {removed_value_safe}")
    print(my_dict)
    """
    list_of_keys=[]
    for key in r.keys():
        list_of_keys.append(key)    
    overlap=True
    while overlap:
        overlap=False
        r=sort_my_dict(r)
        keys_to_remove=[]        
        for index in range(len(list_of_keys)-1):
            Rc=[]
            # Which is larger, r[index] or r[index+1]?
            if ((r[list_of_keys[index]][1]-r[list_of_keys[index]][0])>(r[list_of_keys[index+1]][1]-r[list_of_keys[index+1]][0])): # r[index] is greater
                rai=list_of_keys[index]
                rbi=list_of_keys[index+1]
                Ra=r[rai]
                Rb=r[rbi]
                
            else:
                rai=list_of_keys[index+1]
                rbi=list_of_keys[index]
                Rb=r[rbi]
                Ra=r[rai]            
            # Ra is the larger of the two intervals
            if (Ra[0]<Rb[0]<Ra[1]) or (Ra[0]<Rb[1]<Ra[1]):             
                if not overlap:
                    overlap=True
                    # Calculate resultant range, and replace Ra with Rc.
                    Rc.append(min(Ra[0],Rb[0]))
                    Rc.append(max(Ra[1],Rb[1]))
                    r[rai]=Rc
                    keys_to_remove.append(rbi)
        if overlap:
            for ktr in keys_to_remove:
                r.pop(ktr)
                list_of_keys.remove(ktr)
    
    return r

def sort_my_dict(r):
    swapped = True
    unsorted_list=[]
    for key in r.keys():
        unsorted_list.append(r[key])
    unsorted_list.sort()
    sorted_list=unsorted_list
    keylist=list(r.keys())
    for keylistindex in range(len(r.keys())):
        r[keylist[keylistindex]]=sorted_list[keylistindex]
    
    return r
def report_error(output="None added."):
    with open("error.log", 'a') as err:
        err.write(f"{output}\n")
    return


def write_result(output="Args not passed."):
    with open("result.log", 'a') as result:
        result.write(f"{output}\n")
    return

def main():
    id_ranges=get_file_data()
    current_sum=0
    for key in id_ranges.keys():
        lower=id_ranges[key].split('-')[0]
        upper=id_ranges[key].split('-')[1]
        new_ranges=[]
        new_ranges.append(int(lower))
        new_ranges.append(int(upper))
        id_ranges[key]=new_ranges
    id_ranges=merge_intervals(id_ranges)
    for main_key in id_ranges.keys():
        current_sum+=id_ranges[main_key][1]-id_ranges[main_key][0] +1


    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")

# 432577839375365 Too high.
# 363576316169882 That's not right.