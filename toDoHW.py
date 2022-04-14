import datetime

def check_distance(someday):
    today = datetime.date.today()
    res = someday - today
    return int(res.days)
    
def main():
    dic = {}
    temp = []
    ref = 0
    with open ('to_do_HW.txt', 'r') as file:
        
        for line in file:
            print(line.split()[0] + ": ", end="")
            for word in line.split()[1:]:

                if  word[0].isdigit():
                    for num in word.split("."):
                        temp.append(int(num))

                else:
                    print(word + ": ", end="")

            someday = datetime.date(temp[-1],temp[-2],temp[-3])
            check_distance(someday)
            
            
            if (check_distance(someday) == 0):
                print("WARNING!!! ", end="")
            print(check_distance(someday) , "days left for submit!")
        
        

main()
