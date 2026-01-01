#This is an unknown game
import random
import time
print("-                                                                                              -")
print("------------------------------------Welcome to [Race to 20] Game--------------------------------")
print("-                                                                                              -")
print()
time.sleep(3)
person1=[]
score_person1=0

person2=[]
score_person2=0

person3=[]
score_person3=0

person4=[]
score_person4=0

print("----------------------------------------------")
print("-In this Game every Person will get 5 chances-")
print("----------------------------------------------")
print()
time.sleep(3)

print("--------------------------------------------------------------")
print("-In the chances every person will get a number between (1 to 6)")
print("--------------------------------------------------------------")
print()
time.sleep(3)

print("--------------------------------------------------------------- -----")
print("-The person who will get 20 Point first will be considered as winner.")
print("---------------------------------------------------------------------")
print()
time.sleep(3)
print("-------------------------")
print("-So let's start the Game.")
print("-------------------------")
print()

#loop for finding winner
flag=False
for i in range(5):
    print("------------------------------------")
    print(f"----- {i+1} Round will start soon-------")
    print("------------------------------------")
    print()
    time.sleep(3)

    person1.append(random.randint(1,6))
    score_person1+=person1[i]
    if score_person1 >= 20:
        print("-                                           -")
        print("----------Person-1 is the Winner!------------")
        print("-                                           -")
        print(person1)
        flag=True
        break
    else:
        pass
        

    person2.append(random.randint(1,6))
    score_person2+=person2[i]
    if score_person2 >= 20:
        print("-                                           -")
        print("----------Person-2 is the Winner!------------")
        print("-                                           -")
        print(person2)
        flag=True
        break
    else:
        pass

    person3.append(random.randint(1,6))
    score_person3+=person3[i]
    if score_person3 >= 20:
        print("-                                           -")
        print("----------Person-3 is the Winner!------------")
        print("-                                           -")
        print(person3)
        flag=True
        break
    else:
        pass

    person4.append(random.randint(1,6))
    score_person4+=person4[i]
    if score_person4 >= 20:
        print("-                                           -")
        print("----------Person-4 is the Winner!------------")
        print("-                                           -")
        print(person4)
        flag=True
        break
    else:
        pass
    print("----------------------------------------------")
    print(f"--After the {i+1} Round score of each person------")
    print("----------------------------------------------")
    print(f"{person1} | Total Score:{score_person1}")
    print(f"{person2} | Total Score:{score_person2}")
    print(f"{person3} | Total Score:{score_person3}")
    print(f"{person4} | Total Score:{score_person4}")
#if there is no winner
if not flag:
    print("None of them score 20 points!.It's a draw.")
print("End of the Game.")    