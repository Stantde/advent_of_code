"""
Day 2 Advent of Code 2025
Name: Demetrius Stanton
Date: 12-02-2025
"""
"""
Outline: Based on command-line args, input , incrementing
counter each time the 'zero-th' position is the result of the operation.

Expected outcome from test.txt is 3.
"""
import sys

def get_file_data():
    # Get command line args.
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

def separate_IDs_by_commas(ID_ranges):
    ID=[]
    for key in ID_ranges.keys():
        value_ranges=ID_ranges[key].split(',')
        for value in value_ranges:
            if value:
                ID.append(value)

    return ID

def validate_IDs(ID):
    first=int(ID.split('-')[0])
    last=int(ID.split('-')[1])
    invalid_IDs=[]
    if first<last:
        lower_bound=first
        upper_bound=last
    else:
        report_error(f"first {first}, was not less than {last}!")
    #do I need to search for pallindromes?
    for i in range(lower_bound,upper_bound+1):

        if str(i)[0]=='0':
            report_error(f"found number starting with 0: {str(i)}")
            invalid_IDs.append(i)
        # invalid IDs are any ID which is made only of some sequence of digits repeated twice.
        max_length=len(str(i))
        for start in range(max_length):
            for end in range(start, max_length):
                some_sequence_of_digits=str(i)[start:end]
                for rnd in range(2, max_length+1):
                    try:
                        if i == 80808:
                            ...
                        if (i==int(rnd*some_sequence_of_digits)) and some_sequence_of_digits[0]!='0':
                            if str(i) not in invalid_IDs:
                                #write_result(f"range: {ID} has invalid ID: {str(i)}")
                                invalid_IDs.append(i)
                    except ValueError:
                        continue


    return invalid_IDs

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
    ID=separate_IDs_by_commas(file_data)
    invalid_IDs=[]
    current_sum=0
    for ID_range in ID:
        for entry in validate_IDs(ID_range):
            if (entry not in invalid_IDs):
                invalid_IDs.append(entry)
                write_result(f"range: {ID_range} has invalid ID: {str(entry)}")
    current_sum=sum(invalid_IDs)
    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")
