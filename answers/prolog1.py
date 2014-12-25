class Node:
	#variables
	next = -1
	value = -1
	def __init__(self,value=-1,next=-1,):
		self.next = next
		self.value = value
	#fxns
	def setValue(self, value):
		self.value = value
	def setNext(self, next):
		self.next = next
		
def packDupsIntoSublists(list):
	if list is None or not list:
		print("\tSorry, list was null")
		return
	i = 1
	returnList = []
	currentVar = list[0]
	currentList = [list[0]]
	#print(list)
	while i < len(list):																
		#print(i, "list[i] = ", list[i])
		if list[i] == currentVar:
			#print("i = ", list[i])
			currentList.append(list[i])
			#print(currentList)
		else:
			returnList.append(currentList)
			currentList = [list[i]]
		currentVar = list[i]
		i+=1			
	#print("len = ",len(currentList))
	if len(currentList) > 0:#check if the last part was left out of the loop
		returnList.append(currentList)
	return returnList

def encode1(list):
	if list is None or not list:
		print("\t Sorry, list wasn't null entering encode")
		return None
	i = 0
	while i < len(list):
		sublistLength = len(list[i])
		if sublistLength == 1:
			list[i] = [list[i][0]]
		else:
			list[i] = [sublistLength, list[i][0]]
		i+=1
	return list

x = ['a','a','b','a','c','a','c','c','c','c']
return_list = packDupsIntoSublists(x)
print(return_list)
print(encode1(return_list),"\n")

x = []
return_list = packDupsIntoSublists(x)
print(return_list)
print(encode1(return_list),"\n")

x = ["1"]
return_list = packDupsIntoSublists(x)
print(return_list)
print(encode1(return_list),"\n")

#x = [Node(0), Node(1), Node(2), Node(3), Node(4)]
#c = 0
#while c < len(x) - 1:
#	x[c].next = x[c+1]
#	print(x[c].value)
#	if(x[c].next != -1):
#		print("next is ",x[c].next.value)
#	c += 1
#print(x[c].value, x[c].next)
