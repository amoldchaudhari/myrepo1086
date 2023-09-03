# Array Initialization:

# Create an empty list in Python and add elements to it to create an array of integers. Demonstrate how to append, insert, and remove elements from the array.
listNum = []


def addElementQueue(queueName, num):
    queueName.append(num)

def retrieveElementQueue(queueName):
    item = queueName[0]
    queueName.pop(0)
    return item
def searchandRetrieve(QueueName, element):
    newqueue = []
    flag = 0
    returnIndex = 0
    for index in range(0, len(QueueName)):
        if (QueueName[0] == element):
            flag = 1
            retrieveElementQueue(QueueName)
            returnIndex = index

        else:
            if (flag == 0):
                addElementQueue(newqueue, QueueName[0])
                print("newuqeue", newqueue)

                retrieveElementQueue(QueueName)
    QueueName = newqueue+QueueName
    print(QueueName)
    return returnIndex
addElementQueue(listNum,25)
addElementQueue(listNum,27)
addElementQueue(listNum,29)
addElementQueue(listNum,40)
addElementQueue(listNum,42)
print(listNum , "appended list")
retrieveElementQueue(listNum)
print(listNum)
searchandRetrieve(listNum,40)



# Linked List Creation:

# Implement a basic singly linked list class in Python. Include methods for appending nodes, inserting nodes at specific positions, and printing the linked list.
# Linked List Operations:

# Write a Python function to reverse a singly linked list in-place. Provide both iterative and recursive solutions.
# Array Searching:

# Given an array of integers and a target value, write a Python function to find the index of the target value in the array using binary search. Ensure that the array is sorted before applying binary search.
# Linked List Cycle Detection:

# Create a Python function to detect if a given linked list contains a cycle. Implement Floyd's Tortoise and Hare algorithm to solve this problem efficiently