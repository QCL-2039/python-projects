import time

def time_show(start,end):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Times up")        
        


start=int(input("Enter the starting time:"))
end=int(input("Enter th ending time"))
time_show(start,end)

