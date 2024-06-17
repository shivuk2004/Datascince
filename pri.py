from threading import*
from time import sleep
class odd(Thread):
    def run(self):
        for i in range():
           print(i)
           sleep(2)
class even(Thread):
    def run(self):
        for i in range(2,11,2):
           print(i)
           sleep(2)
            
odd=odd()
even=even()
odd.start()
sleep(2)
even.start()
print("goood bye")
   
