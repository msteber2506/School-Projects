class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext

    def __str__(self):
        pass

class LinkedList:
    def __init__(self):
        self.linkedList = []
        #self.firstNode = self.linkedList[0]

    def isEmpty(self):
        return len(self.linkedList) == 0

    def __len__(self):
        return len(self.linkedList)

    def __getitem__(self,index):
        return self.linkedList[index].getData()

    def search(self,data):
        for node in self.linkedList:
            if node.getData() == data:
                return data
            return None

    def __str__(self):
        return "bruh"

    def append(self,data):
        newNode = Node(data)
        self.linkedList.append(newNode)

    def remove(self,data):
        for node in self.linkedList:
            if node.getData() == data:
                self.linkedList.remove(node)

    