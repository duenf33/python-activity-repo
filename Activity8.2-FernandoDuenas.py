'''
Activity 8

- Write a Program to imitate a Traffic light. Think about the information you need to generate to make your program mimic the real world.

'''

import time

class color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    AMBER = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

print(f"{color.GREEN}CAUTION!! Vehicles crossing.{color.ENDC}")
button = input("Do you need to cross the road? yes or no? - ")

if button == "yes":
   countdown = 3
   for count in reversed(range(1, countdown + 1)):
      print(count)
      time.sleep(1)

   print(f"{color.AMBER}Prepare to stop!{color.ENDC}")
   time.sleep(2)
   print(f"{color.RED}STOP!!{color.ENDC}")
   time.sleep(2)

elif button == "no":
   time.sleep(2)
   print(f"{color.BLUE}Have a nice day.{color.ENDC}")
   time.sleep(2)