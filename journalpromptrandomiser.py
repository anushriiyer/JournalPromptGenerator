import random
import time
import os

def promptDay():
    donelist2 = open("memfile.txt").readlines()
    num = donelist2.count("Y\n")
    return num + 1

day = promptDay()
print("Hello Anushri!")
time.sleep(1)
print("Welcome to Day " + str(day) + " / 1000" )
time.sleep(1)
print("Here is your prompt for the day:\n")
time.sleep(1)

for i in range (3):
    print('.')
    time.sleep(0.5)

print('\n')
time.sleep(1)
promptlist = open("prompts.txt").readlines()
#print(promptlist)
todayspromptno = random.choice(range(len(promptlist)))
todaysprompt = promptlist[todayspromptno]
print(todaysprompt)

time.sleep(600)
# play sound
file = "chime.mp3"
os.system("afplay " + file)
print("Have a great day :)")

donelist = open("memfile.txt").readlines()
#print(len(donelist))
donelist[todayspromptno] = "Y\n"
with open('memfile.txt', 'w', encoding='utf-8') as file:
    file.writelines(donelist)
