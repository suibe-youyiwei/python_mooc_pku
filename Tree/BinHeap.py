class BinHeap:
	def _init_(self):
		self.heapList = [0] #表首下标为0无用
		self.currentSize = 0

	def insert(self,key):
		self.heapList.append(k)
		self.currentSize+=1
		self.percUp(self.currentSize)

	def percUp(self,i):
		while i//2>0:
			if self.heapList[i]<self.heapList[i//2]:
				tmp = self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i//2

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize-=1
		self.heapList.pop()
		self.percDown(1) #下沉
		return retval

	def percDown(self,i):
		while i*2<=self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i]>self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self,i): #获得较小子节点
		if i*2+1>self.currentSize:
			return i*2
		else:
			if self.heapList[i*2+1]>self.heapList[i*2]:
				return i*2
			else:
				return i*2+1

	def buildHeap(self,lst:list): #从无序表产生堆
		i = len(lst)//2
		self.currentSize = len(lst)
		self.heapList = [0]+lst[:]
		while i>0:
			self.percDown(i)
			i-=1

	#进行堆排序
	def HeapSort(self,alist):
		self.buildHeap(alist) #建立小堆顶
		res = []
		while self.currentSize>0:
			self.heapList[1],self.heapList[-1] = self.heapList[-1],self.heapList[1]
			res.append(self.heapList.pop())
			self.currentSize-=1
			self.percDown(1)
		return res




