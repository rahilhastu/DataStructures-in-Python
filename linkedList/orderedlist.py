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
		
	def isEmpty(self):
		return self.head == None

	def size(self):
		current = self.head
		size = 0
		while current!=None:
			count+=1
			current = current.getNext()
		return count


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
			print current.getData(),
			current = current.getNext()
		print 

	def search(self,item):
		current = self.head
		flag = False
		while current!=None and not flag:
			if current.getData()==item:
				flag = True
			elif current.getData()>item:
				flag=True
			else:
				current=current.getNext()
		return flag

	def deleteByItem(self,item):
		current = self.head
		previous =None
		found = False
		while current!=None and not found:
			if current.getData()==item:
				found = True
				print 'Item %d Found\n' %(item)

			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
	
	def deleteByPosition(self,pos):
		current = self.head
		for i in range(pos-2):
			current = current.getNext()

		current.setNext(current.getNext().getNext())

