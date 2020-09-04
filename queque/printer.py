import random
from queue import Queue

class Printer():
    def __init__(self,ppm):
        self.pagerate = ppm #打印速度
        self.currentTask = None #打印任务
        self.timeRemaining = 0 #任务倒计时

    #打印机打印一秒
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask = None
    #定义打印机繁忙
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    #打印新作业
    def startNew(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate

class Task():
    def __init__(self,time):
        self.timestamp = time #生成时间戳
        self.pages = random.randrange(1,21) #生成打印页数

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime - self.timestamp

#1/180概率生成作业
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

#进行模拟
#numSeconds为模拟时间，pagesPerMinute为打印机速度ppm
def simulation(numSeconds,pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNew(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d task remaining."%(averageWait,printQueue.size()))

for i in range(10):
    simulation(3600,10)