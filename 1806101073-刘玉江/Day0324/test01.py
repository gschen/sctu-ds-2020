class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class List():
    def __init__(self):
        self.head = Node(-1)
    def insert_before(self,data):
        for i in data:
            node = Node(i)
            if self.head.next == None:
                self.head.next = node
            else:
                node.next = self.head.next
                self.head.next = node
    def insert_tail(self,data):
        tail = None
        for i in data:
            node = Node(i)
            if self.head.next == None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node
    def print_list(self):
        print("链表：")
        temp = self.head.next
        new_list = []
        while temp is not None:
            new_list.append(temp.value)
            temp = temp.next
        return new_list


if __name__ == "__main__":
    node = Node
    nums = [1,2,3,4,5,6]
    list = List()
    #list.insert_before(nums)
    #print(list.print_list())
    list.insert_tail(nums)
    print(list.print_list())



