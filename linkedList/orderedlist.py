class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next=None
	
	def getData(self):
		return self.data
	
	def getNext(self):
		return self.next
	
	def setData(self,newData):
		self.data = newData
	
	def setNext(self,newNext):
		self.next = newNext
		
class OrderedList:

	def __init__(self):
		self.head = None

	def add(self,item):
		current = self.head
		stop = False
		previous = None
		while current!=None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()
		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(previous.getNext())
			previous.setNext(temp)

	def printq(self):
		current = self.head
		while current!=None:
			print current.getData()
			current = current.getNext()
