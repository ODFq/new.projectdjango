
from audioop import bias
from mailbox import NoSuchMailboxError
import os
from tracemalloc import start
#if os.path.exists("myfile.txt"):
#   os.remove("myfile.txt")
#else:
#   print("The file does not exist")
#os.rmdir("myfolder")]






#os.remove("text.txt")
#f=open("text.txt","w")
#f.write('darsingni bajar')

#for x in f:
#   print(x)
#print(f.readline())
#print(f.readline())
#f.close()
#f=open("text.txt","r")
#print(f.read())
#f=open("myfile.txt","x")
#a="xhgshjjkls"
#for harf in a:
#    print(harf)


"""class Sinf:
    def __init__(self,oquvchilar,rahbar,sinf_nomeri) -> None:
        self.oquvchilar=oquvchilar
        self.rahbar=rahbar
        self.sinf_nomeri=sinf_nomeri
    def __str__(self) -> str:
        return "oquvchi:{},rahbar:{},sinf_nomeri:{}".format(self.oquvchilar,self.rahbar,self.sinf_nomeri)
class sinf_malumoti(Sinf):
    def __init__(self, oquvchilar, rahbar, sinf_nomeri,sinf_sardori) -> None:
        super().__init__(oquvchilar, rahbar, sinf_nomeri)
        self.sinf_sardori=sinf_sardori
    def __str__(self) -> str:
       
        text= super(Sinf,self).__str__()
        text+=",guruh:{}".format(self.sinf_sardori)
        return text

        return text
sinf1=sinf_malumoti(32,"Yusupov",4,"Jaxonova")
print(sinf1)"""
'''import threading
def func():
    for i in range(90):
        print("hello")
def func2():
    for i in range(90):
        print("hi") 

t=threading.Thread(target=func)
t1=threading.Thread(target=func2)
python 
t.start()
t1.start()'''
import threading as thr
import time

def birinchi():
    print("1ishni boshladi")
    time.sleep(2)
    print("ishni yakunladi")
def ikkinchi():
    print("2ishni boshladi")
    print("2ishni yakunladi")
t1 =  thr.Thread(target=birinchi,daemon = True)
t2 = thr.Thread(target=ikkinchi)
t1.start()
t2.start()


event = thr.Event()

def jarayon():
    print("Djangoni o'rnatish")
    event.wait()
    print("Djangoni o'rnatish boshlandi")

t1 = thr.Thread(target=jarayon)
t1 = start()

sorov = input("Djangoni o'rnatish boshlansinmi: (h)")
if sorov == "h":
    event.set()



        
        

