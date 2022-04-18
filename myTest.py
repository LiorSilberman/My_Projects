import datetime
import os
import random

# calculate days for submit home work
def days_to_submit(someday):
    today = datetime.date.today()
    res = someday - today
    return int(res.days)

# read from file and make sorted dict
def read_file(file):
    temp = []
    dic = {}
    
    for line in file:
        temp.append(line.split())
        
    for lst in temp[1:]:
            date = lst[1].split('.')
            
            someday = datetime.date(int(date[-1]),int(date[-2]),int(date[-3]))
            days = days_to_submit(someday)
            dic[days] = lst
            
    dic = dict(sorted(dic.items(), key=lambda item: item[0]))
    file.close()
    return dic

# print from dict 
def print_dic(dic):
    print("\nTo Do List:")
    for k,v in dic.items():
        print("\t" + v[0]+" - "+ v[2] + ": " + str(k) , "days for submit!")
        
# update txt file 
def handle_dict(dic):
    for k,v in dic.items():
        if k < 0:
            print("\ndid you submit" , v[2], "in", v[0] + " until " + v[1] + "? (yes/no)", end="")
            answer = input()
            
            if answer == "yes":
                
                arr = ["you are on fire today!", "you are the man", "good for you", "oh yeah"]
                print(random.choice(arr))
                
                with open("to_do_HW.txt", "r") as inp:
                    with open("temp.txt", "w") as output:
                        # iterate all lines from file
                        for line in inp:
                            compare_line = v[0] +"\t" + v[1] + "\t\t" + v[2]
                            
                            if line.strip("\n") != compare_line:
                                output.write(line)

                # replace file with original name
                os.replace('temp.txt', 'to_do_HW.txt')
                inp.close()
                output.close()
                
            
            if answer == "no":
                continue

def main():
    with open ('to_do_HW.txt', 'r') as file:
        dic = read_file(file)
        handle_dict(dic)
        file.close()

    with open ('to_do_HW.txt', 'r') as file:
        print_dic(read_file(file))

main()