"""
Day 6 Advent of Code 2025
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
    foo={}    
    count =0
    with open(filename,'r') as f:
        for line in f:
            foo_line=[]
            #foo[count]=[]
            MAGIC_NUMBER=5
            tmp=3785/MAGIC_NUMBER
            for i in range(int(3785/MAGIC_NUMBER)):
                foo_line.append(line[i*MAGIC_NUMBER:i*MAGIC_NUMBER+MAGIC_NUMBER-1])
            foo[count]=foo_line
            if foo[count][0].strip() in ['+','*']:
                foo['sign']= foo[count]
                foo.pop(count, None)
            tmp=len(line)
            count+=1

    return foo 


def report_error(output="None added."):
    with open("error.log", 'a') as err:
        err.write(f"{output}\n")
    return


def write_result(output="Args not passed."):
    with open("result.log", 'a') as result:
        result.write(f"{output}\n")
    return
def get_sum(homework_set):
    grand_total=0    
    try:
        for pset in range(len(homework_set[0])):
            sign = homework_set['sign'][pset].strip()
            total=0
            unorganized_terms=[]
            organized_terms=[]
            for key in range(len(homework_set.keys())-1):
                unorganized_terms.append(homework_set[key][pset])
                """if total==0:
                    total=int(homework_set[key][pset])
                elif sign=='+':
                    total+=int(homework_set[key][pset])                    
                elif sign=='*':
                    total*=int(homework_set[key][pset])"""
            max_length=0
            for term in unorganized_terms:
                if max_length == 0:
                    max_length=len(term)
                if len(term)>max_length:
                    max_length=len(term)
            baz=[]
            not_empty=True
            while not_empty:                
                not_empty=False
                digit=1
                i=0
                new_num=0
                for term in unorganized_terms: # ['123', '45', '6'] for example sign =*, expect 356*24*1=8544
                    if term:
                        try:
                            num=int(term[-1])%10
                        except ValueError:
                            num=0
                        unorganized_terms[i]=unorganized_terms[i][:len(term)-1] #expect one less 
                        not_empty=True
                    else: 
                        num=0
                    new_num+=digit*num
                    digit*=10
                    i+=1
                if int(str(new_num)[::-1])>0:
                    baz.append(int(str(new_num)[::-1]))
            for term in baz:
                if total==0:
                    total=term
                elif sign=='+':
                    total+=term
                elif sign=='*':
                    total*=term
            grand_total+=total
    except KeyError:
            pass
        

    
    return grand_total

def main():
    file_data=get_file_data()
    
    current_sum=get_sum(file_data)    


    return str(current_sum)

if __name__=='__main__':
    print(f"The sum is: {main()}.")
