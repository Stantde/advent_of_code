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
    overlap=True
    while overlap:
        current_ranges=[]    
        overlap=False
        for primary in list(r.keys()):
            c=r[primary][0]
            d=r[primary][1]
            if current_ranges:
                updated_range=False
                for idr in current_ranges:
                    a=idr[0]
                    b=idr[1]
                    if (a<=c<=b)and(a<=d<=b): #ab includes cd
                        # the range under evaluation already exists. 
                        # remove the current range's key from dict 
                        # and mark changed.
                        # dont add to currrent_range
                        r.pop(primary, None)
                        overlap=True
                        updated_range=True
                        break
                    elif (c<=a<=d)and(c<=b<=d):# cd includes ab
                        # the range under evaluation completely contains a previous range.
                        # this is a curious condition. I feel like changing the prior range can affect any check last performed.
                        # If it does, wouldn't those changes be caught on later iterations?
                        # update previous range to match current range both in primary dict and current range.
                        for key, value in r.items():
                            if value == idr:
                                r[key]=r[primary]
                                r.pop(primary, None)
                                overlap=True
                                updated_range=True
                                break
                        
                    elif (c<=a<=d and d<=b):# a only bw cd
                        # Extend range of cd to cb
                        d=b
                        r[primary][1]=b
                        overlap=True
                        current_ranges.append([c,d])
                        updated_range=True                        
                        break
                        
                    elif (c<=b<=d and a<=c):# b bwt cd
                        # Extend range of cd to ad
                        c=a
                        #r[primary][0]=a
                        overlap=True
                        current_ranges.append([c,d])
                        updated_range=True
                        break
                if not updated_range:
                    current_ranges.append(r[primary])    

            else:
                current_ranges.append(r[primary])
        current_ranges.sort()
        count = 0
        list_to_remove=[]
        for sr in range(len(current_ranges)-1):
            if current_ranges[sr][0]==current_ranges[sr+1] [0]:
                current_ranges[sr][1]=max(current_ranges[sr+1] [1],current_ranges[sr][1])
                current_ranges[sr+1][1]=max(current_ranges[sr+1] [1],current_ranges[sr][1])
                list_to_remove.append(current_ranges[sr])
        for i in list_to_remove:
            current_ranges.remove(i)
        r={}
        count=0
        for i in current_ranges:
            r[count]=current_ranges[count]
            count+=1
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
    id_ranges,ids=get_file_data()
    current_sum=0
    for key in id_ranges.keys():
        lower=id_ranges[key].split('-')[0]
        upper=id_ranges[key].split('-')[1]
        new_ranges=[]
        new_ranges.append(int(lower))
        new_ranges.append(int(upper))
        id_ranges[key]=new_ranges
    id_ranges=merge_intervals(id_ranges)
    for main_key in range(len(id_ranges.keys())):
        current_sum+=id_ranges[main_key][1]-id_ranges[main_key][0] +1


    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")
