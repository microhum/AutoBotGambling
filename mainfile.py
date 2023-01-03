import select
import sys
import time
import random
import cooldowns as cd
import pynput
from pynput.keyboard import Key, Controller
import config
keyboard = Controller()
pmtypes = ["f", "r", "i", "c", "k"]


def type_send(msg):
    print("sent",msg)
    keyboard.type(str(msg))
    time.sleep(2)
    keyboard.press(Key.enter)

def print_work(scheduler):
    type_send(";work")
    scheduler.run_after(print_work, cd.work_cooldown)

def print_slut(scheduler):
    type_send(";slut")
    scheduler.run_after(print_slut, cd.slut_cooldown)

def print_crime(scheduler):
    type_send(";crime")
    scheduler.run_after(print_crime, cd.crime_cooldown)

def print_dep(scheduler):
    type_send(";dep all")
    scheduler.run_after(print_dep, cd.dep_cooldown)

class Scheduler:
    def __init__(self):
        self.ready = []
        self.waiting = []

    def run_soon(self, task):
        self.waiting.append((task, 0))

    def run_after(self, task, delay):
        self.waiting.append((task, time.time() + delay))

    def run_until_complete(self):
        while self.ready or self.waiting:
            while self.ready:
                self.ready.pop()(self)
                time.sleep(random.randint(3,7))
            for i in range(len(self.waiting) - 1, -1, -1):
                task, start_after = self.waiting[i]
                if start_after < time.time():
                    self.ready.append(task)
                    del self.waiting[i]
print("Preparing run")
s = Scheduler()
time.sleep(5) #activate your window where you need to type within 5 sec
print("Start")
if config.work:
    s.run_soon(print_work)
if config.slut:
    s.run_soon(print_slut)
if config.crime:
    s.run_soon(print_crime)
if config.dep:
    s.run_soon(print_dep)
s.run_until_complete()

#use async in future
