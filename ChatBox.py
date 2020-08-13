import time

def myName():
  print(" Created by lav_sarkari ")

def welcome():
  print("      Welcome to ChatBox ")

def decorador(func):
  print("")
  print("-"*39)
  func()
  print("-"*39)
  print("")

decorador(welcome)
time.sleep(2)
decorador(myName)
time.sleep(1)
w="""
  ------------
  |Writing...|
  ------------
  """
print(w)
time.sleep(4)
print("Hello, My name is Chatrum ")
time.sleep(1)
print(w)
time.sleep(3)
name = input("What's your name? ")
time.sleep(1)
print(w)
time.sleep(5)
print(f"Oh, Hi {name} nice to meet you! And nice name")
time.sleep(1)
print(w)
time.sleep(3.5)

f = input("How do you feel today? ")
time.sleep(1)
print(w)
time.sleep(3)
if f == "fine":
  print("Oh, that's really good! ")

elif f == "bad":
  print("Oh, that's not good ")
time.sleep(1)
print(w)
time.sleep(3)
age = int(input("How old are you my friend? "))
epoc = ""
if age < 25:
  epoc = "young"
elif age > 25 and age < 60:
  epoc = "adult"
elif age > 60 and age < 100:
  epoc = "old"
else:
  epoc = "very old"
time.sleep(1)
print(w)
time.sleep(5.5)
print(f"Oh {age} years old, you are {epoc} my friend!")
time.sleep(1)
print(w)
time.sleep(3)
print("I'm 16 years old")
time.sleep(1)
print(w)
time.sleep(6)
print("I think I should go now ")
