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



class unoderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count+=1
			current = current.getNext()
		return count

	def search(self,item):
		current = self.head
		flag = False
		while current != None and not flag:
			if current.getData()==item:
				flag = True
			else:
				current = current.getNext()
		return flag

	def remove(self,item):
		current = self.head
		previous =None
		found = False
		while current!=None and not found:
			if current.getData()==item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def printq(self):
		current = self.head
		while current!=None:
			print current.getData(),
			current = current.getNext()
